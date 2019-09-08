import numpy as np 

# energy
w = -30  # J

# charge
q = np.array([6, -3])  # C

# voltage
v = w/q
print(f"the voltage drop is {v[0]:.4f} and {v[1]:.4f} for 'q = 6 C' and 'q = -3 C', respectively")