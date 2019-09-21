from sympy import *
init_printing(use_unicode=True)

# R = oo
L = 20
C = 0.2
Is = 10

alpha = 0
omega0 = 1/sqrt(L*C)

i0 = 0
v0 = 0
didt0 = 0

t = symbols('t')
i = symbols('i', cls=Function)
diffeq = Eq(i(t).diff(t, t) + 2*alpha*i(t).diff(t) + omega0**2*i(t), Is/(L*C))
soln = dsolve(diffeq, i(t))
pprint(soln)
constants = solve([soln.rhs.subs(t, 0) - i0, soln.rhs.diff(t).subs(t, 0) - didt0])
pprint(constants)