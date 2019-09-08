from sympy import *

# define symbols
t = symbols("t")

# define expressions
p = 30e-3*cos(t)**2  # W
v = 15*cos(t)  # V

# results
i = p/v
R = v/i

print("Current is: (A)")
pprint(i)
print(f"Resistance is: {R.evalf():.4f} ohm")