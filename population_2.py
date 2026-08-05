# important libs and constants
import plot_utils as p
import functions as fct
import ODE_solver as odes
import numpy as np
import random
import csv
import os
import h5py

os.makedirs("sol_pop_2", exist_ok=True)
G = 6.674e-11  # N*m^2/Kg^2
Msolar = 1.989e30  # kg
Rsolar = 6.957e8  # in m
c = 299792458.0  # m/s
counter = 0
AU = 149597870700 # in m

# Open the outputfile once, before loops
with open("possible_output_pop_2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Write the header only once
    writer.writerow(["ID", "m_WR/M_Sun", "m_companion/M_Sun", "k", 'Q', 'initial separation a0 (m)', 'WR star Radius R_WR', 'R_WR/a0', 'initial spin Omega0 (Hz)', 'lifetime (years)',
                     'tidal function timescale (years)', "gw timescale (years)", 'initial frequency f0 (Hz)', 'f_final (Hz)', 'f_min (Hz)', 'Omega_final (Hz)', 'final angular momentum J (kg m^2/s)', 'spin parameter a_spin', 'final separation a_final (m)', 'minimum separation a_min (m)'])

    with h5py.File('K0559Phal250710_jwst0.hdf5', 'r') as d:
    
        # Use d.keys() to see the actual names
        m_wr_all = d['mass_1?'][:]         # WR masses in Solar Masses
        m_bh_all = d['mass_2?'][:]         # BH masses in Solar Masses
        a0_all = d['a_orb_evol'][:]        # Initial separations (usually in AU or Rsun)
        lifetimes_all = d['lifetime(calculate from mass? or evolve_time?)'][:] # Lifetime in years
        is_BBH_all = d['is_BBH'][:]        #is it a BBH

        num_systems = len(m_wr_all)

        # loop through the systems in the simulation
        for i in random.sample(range(num_systems), 10000):
            
            # physical parameters for the specific binary
            m1 = m_wr_all[i] * Msolar #in Kg
            m2 = m_bh_all[i] * Msolar #in Kg
            a0 = a0_all[i] * Rsolar  # CHECK UNITS BASED ON THE FILE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! point is i want solar radii for my math
            lifetime = lifetimes_all[i]
            is_BBH = is_BBH_all[i]
            
            # parameters i still pick myself
            if is_BBH == 1:
                for rg2 in [0.1]:
                    for k in [0.001]:
                        for Q in [1e4, 1e5, 1e6, 1e7]:
                            q = m1/m2
                            
                            # CHECK IF RADIUS IN THE FILE IF YES NO NEED
                            RWR1 = fct.radius_from_mass(
                                m1/Msolar)  # in solar radii
                            R1 = RWR1*Rsolar  # in m

                            a_max = fct.max_separation(
                                1.36e10, m1, m2)  # in m
                            a_min = fct.min_separation(
                                q, RWR1)  # in solar radii
                            a_min_si = a_min*Rsolar  # in m

                            fmax = fct.gw_frequency(a_max, m1, m2)
                            fmin = fct.gw_frequency(a_min_si, m1, m2)

                            T_TF_max = fct.tidal_friction_timescale(
                                m1, m2, Q, k, a_max, RWR1, fmax)
                            T_TF_min = fct.tidal_friction_timescale(
                                m1, m2, Q, k, a_min_si, RWR1, fmin)

                            tfinal = lifetime*365.25*24*3600  # time in s

                            # checking if it's realistic 
                            if a0 <= a_max:
                                f0 = fct.gw_frequency(a0, m1, m2)

                                T_GW = fct.gw_timescale(a0, m1, m2)

                                T_TF = fct.tidal_friction_timescale(
                                    m1, m2, Q, k, a0, RWR1, f0)/(3600*24*365.25)
                                
                                if T_TF <= 100*lifetime:  # assume if it's bigger then it has no hope 

                                    K1 = (18*k/Q)*(m2*(np.pi**(13/3))*(R1**5)) / \
                                        ((G**(5/3))*m1*(m1+m2)**(5/3))
                                    K2 = (3*k/Q)*((m2**2)*(np.pi**3)*(R1**3)) / \
                                        (G*m1*rg2*(m1+m2)**2)

                                    def dfdt(f, Omega):
                                        return K1*(f**(13/3))*(f/2-Omega)

                                    def dOmegadt(f, Omega):
                                        return K2*(f**3)*(f/2-Omega)
                                    
                                    #t_scale = 3.1536e13  # 1 Myr in seconds
                                    #x_scale = 1e-5       # 10 microHz in Hz
                                    #y_scale = 1e-5       # 10 microHz in rad/s (for Omega)

                                    for Omega0 in [1e-5]:
                                        sols = odes.solve_Radau(
                                            dxdt=dfdt, dydt=dOmegadt, x0=f0, y0=Omega0, t0=0, tfinal=tfinal, x_scale=1e-5, y_scale=1e-5, t_scale=tfinal)

                                        # in years
                                        t = sols[0]/(3600*24*365.25)
                                        f = sols[1]  # in Hz
                                        Omega = sols[2]  # in Hz

                                        J = rg2*m1*(R1**2)*Omega[-1]
                                        a_spin = c*J/(G*m1*m1)
                                        a_final = fct.separation_from_gw_frequency(
                                            # final separation in m
                                            f[-1], m1, m2)

                                        if f[-1] <= 2*fmin:
                                            # checking if mass transfer starts but it hasn't for any of the cases I got after correcting the K1 expression

                                            sol_id = f"sol_{counter:05d}"
                                            np.savez(
                                                f"sol_pop_2/{sol_id}.npz", t=t, f=f, Omega=Omega)
                                            counter += 1

                                            # Write one row for this iteration
                                            writer.writerow(
                                                [sol_id, m1/Msolar, m2/Msolar, k, Q, a0, R1, R1/a0, Omega0, lifetime, T_TF, T_GW, f0, f[-1], fmin, Omega[-1], J, a_spin, a_final, a_min_si])
                                            
