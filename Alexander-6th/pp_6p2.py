from sympy import *

C = 10e-6  # F

# define symbols
t = symbols("t")

# define expressions
v = 20*cos(200*t)  # V
i = C*diff(v, t)

print("the current through the capacitor is: (mA)")
pprint(i*1e3)
