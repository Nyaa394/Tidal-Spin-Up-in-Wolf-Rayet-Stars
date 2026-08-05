# important libs and constants
import plot_utils as p
import functions_B as fct  # Make sure this matches filename
import ODE_solver as odes
import numpy as np
import random
import csv
import os

os.makedirs("mod_B_I_sols", exist_ok=True)
G = 6.674e-11  # N*m^2/Kg^2
Msolar = 1.989e30  # kg
Rsolar = 6.957e8  # in m
c = 299792458.0  # m/s
counter = 0

# Open the outputfile once, before loops
with open("mod_B_I_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Write the header only once
    writer.writerow(["ID", "m_WR/M_Sun", "m_companion/M_Sun", "k", 'Q', 'WR star Radius R_WR', 'initial separation a0 (m)', 'final separation (m)', 'R_WR/a0', 'lifetime (years)',
                     'tidal function timescale (years)', "gw timescale (years)", 'initial frequency f0 (Hz)', 'f_final (Hz)', 'initial orb freq (Hz)', 'final orb freq (Hz)', 'initial spin Omega0 (Hz)', 'Omega_final (Hz)', 'final angular momentum J (kg m^2/s)', 'spin parameter a_spin'])

    # shit just got real
    for m1_0 in [random.uniform(10*Msolar, 100*Msolar) for _ in range(100)]:
        for m2 in [random.uniform(20*Msolar, 100*Msolar) for _ in range(100)]:
            for e0 in [0.05, 0.35, 0.65, 0.85]:
                for rg2 in [0.1]:
                    for k in [0.001]:
                        for Q in [1e4, 1e5, 1e6, 1e7]:
                            for lifetime in [1000, 10000, 1e5, 1e6]:
                                for a0 in [1.165e+09, 5.038e+10, 9.959e+10, 1.488e+11]: #taken from graph but made into m

                                    RWR1_0 = fct.radius_from_mass(
                                        m1_0/Msolar)  # in solar radii
                                    R1_0 = RWR1_0*Rsolar  # in m

                                    tfinal = lifetime*365.25*24*3600  # time in s

                                    # checking timescales compared to lifetime, timescale has to be shorter for tides to have time to act

                                    f0 = fct.gw_frequency(a0, m1_0, m2)

                                    T_GW_0 = fct.gw_timescale(a0, m1_0, m2)

                                    T_TF_0 = fct.tidal_friction_timescale(
                                        m1_0, m2, Q, k, a0, RWR1_0, f0)/(3600*24*365.25)  #yes, R in solar radii is fine bc the function converts it. why did i not just use the other? idk but also i'm not touching it for now

                                    if T_TF_0 <= 1000*lifetime:  # assume if it's bigger then it has no hope


                                        #START SOLVER
                                        
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
                                                dxdt=dfdt, dydt=dOmegadt, x0=f0, y0=Omega0, t0=0, tfinal=tfinal, x_scale=1e-5, y_scale=1e-5, t_scale = tfinal)

                                            t = sols[0]/(3600*24*365.25)  # in years
                                            a = sols[1]  # in Hz
                                            Omega = sols[2]  # in Hz
                                            e = sols [3] #verify the numbering later not guaranteed that it won't change
                                            m1 = sols [4]

                                            #END SOLVER

                                            #START IF LOOPS ON ALL SOLUTIONS DO THE REST OF THE CHECKS (a_min, a_max, )

                                            a_max = fct.max_separation(
                                                1.36e10, m1, m2, e0)  # in m
                                            a_min = fct.min_separation(
                                                q, RWR1)  # in solar radii
                                            a_min_si = a_min*Rsolar  # in m

                                            fmax = fct.gw_frequency(a_max, m1, m2)
                                            fmin = fct.gw_frequency(a_min_si, m1, m2)

                                            J = rg2*m1*(R1**2)*Omega[-1]
                                            a_spin = c*J/(G*m1*m1)
                                            a_final = a[-1]
                                            
                                            sol_id = f"sol_{counter:05d}"
                                            np.savez(
                                                f"mod_B_I_sols/{sol_id}.npz", t=t, f=f, Omega=Omega)
                                            counter += 1

                                            # Write one row for this iteration
                                            writer.writerow(
                                                [sol_id, m1/Msolar, m2/Msolar, k, Q, R1, a0, a_final, R1/a0, lifetime, T_TF, T_GW, f0, f_final, f_orb0, f_orb_final, Omega0, Omega[-1], J, a_spin])
                                        
