from sympy import *

# define symbols
t = symbols("t")

# define expressions
v = 20*sin(pi*t)  # V

R = 5e3  # ohm

# results
i = v/R
p = v*i

print("The current is: (A)")
pprint(i)
print("The dissipated power is: (W)")
pprint(p)