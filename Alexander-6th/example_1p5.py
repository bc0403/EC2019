from sympy import *

# define symbols
t = symbols("t")

# define expressions
i = 5*cos(60*pi*t)  # A
v1 = 3*i
v2 = 3*diff(i,t)
p1 = v1*i
p2 = v2*i

# convert sympy expressions to numerical functions
p1_num = lambdify(t, p1, "numpy")
p2_num = lambdify(t, p2, "numpy")

# result
print(f"the power delivered to the element is {p1_num(3e-3):.4f} and {p2_num(3e-3):.4f} W, respectively.")