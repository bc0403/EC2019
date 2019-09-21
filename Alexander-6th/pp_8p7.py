from sympy import *
init_printing(use_unicode=True)

R = 10
L = 2.5
C = 1/40
Vs = 15
alpha = R/(2*L)
omega0 = 1/sqrt(L*C)

v0 = 12
i0 = 0
dvdt0 = 0

t = symbols('t')
v = symbols('v', cls=Function)
diffeq = Eq(v(t).diff(t, t) + 2*alpha*v(t).diff(t) + omega0**2*v(t), Vs/(L*C))
soln = dsolve(diffeq, v(t))
pprint(soln)
constants = solve([soln.rhs.subs(t, 0) - v0, soln.rhs.diff(t).subs(t, 0) - dvdt0])
pprint(constants)
