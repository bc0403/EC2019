from sympy import *

# define symbols
t = symbols("t")

# define expressions
i = 5*cos(60*pi*t)  # A
v1 = 2*i
v2 = 10 + 5*integrate(i, (t, 0, t))
p1 = v1*i
p2 = v2*i

# convert sympy expressions to numerical functions
p1_num = lambdify(t, p1, "numpy")
p2_num = lambdify(t, p2, "numpy")

# result
print(f"the power delivered to the element is {p1_num(5e-3):.4f} and {p2_num(5e-3):.4f} W, respectively.")