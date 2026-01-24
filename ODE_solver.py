# solve stiff non linear ode

# there was an attempt to use sympy dsolve which I will keep for future reference T-T
# import sympy
# t = sympy.symbols('t')
# f = sympy.Function('f')
# Omega = sympy.Function('Omega')
# K1_val = sympy.Float(K1)
# K2_val = sympy.Float(K2)
# eq1 = sympy.Eq(sympy.Derivative(f(t), t), K1_val*(f(t)**(13/3))*(f(t)/2-Omega(t)))
# eq2 = sympy.Eq(sympy.Derivative(Omega(t), t), K2_val*(f(t)**3)*(f(t)/2-Omega(t)))
# sol = sympy.dsolve([eq1, eq2], [f(t), Omega(t)])
# from sympy.solvers.ode.systems import dsolve_system
# sol = dsolve_system([eq1, eq2])
# print(sol)

# ivp version
# scaling factors

# I AM SO GOING TO DIE #dxdt and dydt are functions
def solve_Radau(dxdt, dydt, x0, y0, t0, tfinal, x_scale, y_scale, t_scale):
    from scipy.integrate import solve_ivp
    import numpy as np
    x_scale = x_scale
    y_scale = y_scale
    t_scale = t_scale

    def system_scaled(t_scaled, vars_scaled):
        # scaled variables
        x_scaled, y_scaled = vars_scaled
        # convert back to physical variables
        x = x_scaled * x_scale
        y = y_scaled * y_scale
        t = t_scaled * t_scale

        dx_scaled_dt_scaled = dxdt(x, y) * t_scale / x_scale
        dy_scaled_dt_scaled = dydt(x, y) * t_scale / y_scale
        return [dx_scaled_dt_scaled, dy_scaled_dt_scaled]
    # initial conditions
    x0 = x0
    y0 = y0
    u0_scaled = [x0 / x_scale, y0 / y_scale]
    # time span and evaluation points (scaled)
    t_span = (t0/t_scale, tfinal / t_scale)
    t_eval = np.linspace(t_span[0], t_span[1], 500)
    sol_scaled = solve_ivp(system_scaled, t_span, u0_scaled,
                           t_eval=t_eval, method='Radau')
    sol_t = sol_scaled.t*t_scale
    sol_x = sol_scaled.y[0]*x_scale
    sol_y = sol_scaled.y[1]*y_scale
    return sol_t, sol_x, sol_y


# scaling factors
# f_scale = 1.0
# Omega_scale = 1.0
# t_scale = 1.0  # 1000 * 365.25 * 24 * 3600  # 1000 years in seconds


# def system_scaled(t2, u2):
    # scaled variables
    f2, Omega2 = u2
    # convert back to physical variables
    f = f2 * f_scale
    Omega = Omega2 * Omega_scale
    t = t2 * t_scale  # actually not needed this time bc functions don't depend on t but just in case for the future
    # scaled derivatives
    df2_dt2 = g(f, Omega) * t_scale / f_scale
    dOmega2_dt2 = h(f, Omega) * t_scale / Omega_scale
    return [df2_dt2, dOmega2_dt2]


# initial conditions
# f0 = 1e-9
# Omega0 = 1e-5
# u0_scaled = [f0 / f_scale, Omega0 / Omega_scale]
# time span and evaluation points (scaled)
# t2_span = (0, tfinal / t_scale)
# t2_eval = np.linspace(t2_span[0], t2_span[1], 500)
# sol_scaled = solve_ivp(system_scaled, t2_span, u0_scaled,
    # t_eval=t2_eval, method='Radau')
# print(sol_scaled)
