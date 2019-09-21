from sympy import *
init_printing(use_unicode=True)

i0 = 10
v0 = 0
vL0 = v0 + (-1*i0)*5
didt0 = vL0

alpha = 5/2
omega0 = 1/sqrt(1/9)

t = symbols("t")
i = symbols("i", cls=Function)
diffeq = Eq(i(t).diff(t, t) + 2*alpha*i(t).diff(t) + omega0**2*i(t), 0)
soln = dsolve(diffeq, i(t))
pprint(soln)
constants = solve([soln.rhs.subs(t, 0) - i0, soln.rhs.diff(t).subs(t, 0) - didt0])
pprint(constants)
