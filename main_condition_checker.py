# find m1, m2, a0, k/Q so that Omegafinal >= 0.1*f_orb which is f/2 at tfinal (m1 is mass of main star, m2 mass of companion)

# important libs and constants
import plot_utils as p
import functions as fct
import ODE_solver as odes
import numpy as np
import random
import csv
G = 6.674e-11  # N*m^2/Kg^2
Msolar = 1.989e30  # kg
Rsolar = 6.957e8  # in m
c = 299792458.0  # m/s

# Open the outputfile once, before loops
with open("possible_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Write the header only once
    writer.writerow(["m_WR/M_Sun", "m_companion/M_Sun", "k", 'Q', 'initial separation a0 (m)', 'initial spin Omega0 (Hz)', 'lifetime (years)',
                     'tidal function timescale (years)', 'initial frequency f0 (Hz)', 'f_final (Hz)', 'Omega_final (Hz)', 'final angular momentum J (kg m^2/s)'])

    # shit just got real
    for m1 in [random.uniform(10*Msolar, 100*Msolar) for _ in range(10)]:
        for m2 in [random.uniform(20*Msolar, 100*Msolar) for _ in range(10)]:
            for rg2 in [0.1]:
                for k in [0.001]:
                    for Q in [1e4, 1e5, 1e6, 1e7]:
                        for lifetime in [1000, 5000, 10000, 1e5]:
                            q = m1/m2

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

                            # checking timescales compared to lifetime, timescale has to be shorter for tides to have time to act

                            T_TF = fct.tidal_friction_timescale(
                                m1, m2, Q, k, a_min_si, RWR1, fmin)/(3600*24*365.25)
                            if T_TF <= lifetime:

                                # and now I die

                                K1 = (18*k/Q)*(m2*(np.pi**(13/3))*(R1**5)) / \
                                    ((G**(5/3))*m1*rg2*(m1+m2)**(5/3))
                                K2 = (3*k/Q)*((m2**2)*(np.pi**3)*(R1**3)) / \
                                    (G*m1*rg2*(m1+m2)**2)

                                def dfdt(f, Omega):
                                    return K1*(f**(13/3))*(f/2-Omega)

                                def dOmegadt(f, Omega):
                                    return K2*(f**3)*(f/2-Omega)

                                for a0 in [2*a_min_si, 3*a_min_si, 4*a_min_si, 5*a_min_si]:
                                    f0 = fct.gw_frequency(a0, m1, m2)
                                    for Omega0 in [1e-5]:
                                        sols = odes.solve_Radau(
                                            dxdt=dfdt, dydt=dOmegadt, x0=f0, y0=Omega0, t0=0, tfinal=tfinal, x_scale=1, y_scale=1, t_scale=1)

                                        # in years
                                        t = sols[0]/(3600*24*365.25)
                                        f = sols[1]  # in Hz
                                        Omega = sols[2]  # in Hz
                                        J = rg2*m1*(R1**2)*Omega[-1]

                                        if Omega[-1] >= 0.1*(f[-1]/2):
                                            # Write one row for this iteration
                                            writer.writerow(
                                                [m1/Msolar, m2/Msolar, k, Q, a0, Omega0, lifetime, T_TF, f0, f[-1], Omega[-1], J])
