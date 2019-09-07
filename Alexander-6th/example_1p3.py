from sympy import *

# define symbols
t = symbols('t')

# define expressions
i = 3*t**2 -t  # A
Q = integrate(i, (t, 1, 2))

# result
print(f"the total charge is {Q.evalf():.4f} C")