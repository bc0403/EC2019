# using sympy for symbolic calculate
from sympy import *
init_printing(use_unicode=True)

# define symbols
t = symbols("t")

# define expressions
q = (10 - 10*exp(-2*t))  # mC
i = diff(q, t)

# convert sympy expression to numerical function
i_num = lambdify(t, i, "numpy")

# result
print("The expression of i is: ")
pprint(i)
print(f"and the current at t = 1 s is {i_num(1):.4f} mA")
