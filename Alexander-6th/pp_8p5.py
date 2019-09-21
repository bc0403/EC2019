from sympy import *
init_printing(use_unicode=True)

R = 2
L = 0.4
C = 25e-3
alpha = 1/(2*R*C)
omega0 = 1/sqrt(L*C)

v0 = 0
i0 = 50e-3
iR0 = v0/R
iC0 = -(iR0 + i0)
dvdt0 = iC0/C

t = symbols('t')
v = symbols('v', cls=Function)
diffeq = Eq(v(t).diff(t, t) + 2*alpha*v(t).diff(t) + omega0**2*v(t), 0)
soln = dsolve(diffeq, v(t))
pprint(soln)
constants = solve([soln.rhs.subs(t, 0) - v0, soln.rhs.diff(t).subs(t, 0) - dvdt0])
pprint(constants)
