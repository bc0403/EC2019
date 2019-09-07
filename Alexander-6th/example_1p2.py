# using sympy for symbolic calculate
from sympy import *
init_printing(use_unicode=True)

# define symbols
t = symbols("t")

# define expressions
q = 5*t*sin(4*pi*t)  # mC
i = diff(q, t)

# convert sympy expression to numerical function
i_num = lambdify(t, i, "numpy")

# result
print("The expression of i is: ")
pprint(i)
print(f"and the current at t = 0.5 s is {i_num(0.5):.4f} mA")
