import numpy as np 

# energy
w = 25  # J

# charge
q = np.array([5, -10])  # C

# voltage
v = w/q
print(f"the voltage drop is {v[0]:.4f} and {v[1]:.4f} V for 'q = 5 C' and 'q = -10 C', respectively")