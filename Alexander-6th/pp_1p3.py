from sympy import *

# define symbols
t = symbols('t')

# define expressions
i_1 = 4  # A
i_2 = 4*t**2  # A
Q = integrate(i_1, (t, 0, 1)) + integrate(i_2, (t, 1, 2))

# result
print(f"the total charge is {Q.evalf():.4f} C")