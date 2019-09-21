from sympy import *
init_printing(use_unicode=True)

R = 20
L = 10
C = 4e-3
alpha = 1/(2*R*C)
omega0 = 1/sqrt(L*C)
print(alpha, omega0)

v0 = 0
i0 = 1.5
iR0 = 0
iC0 = -1*i0
dvdt0 = iC0/C

t = symbols('t')
v = symbols('v', cls=Function)
diffeq = Eq(v(t).diff(t, t) + 2*alpha*v(t).diff(t) + omega0**2*v(t), 0)
soln = dsolve(diffeq, v(t))
pprint(soln)
constants = solve([soln.rhs.subs(t, 0) - v0, soln.rhs.diff(t).subs(t, 0) - dvdt0])
pprint(constants)



