import numpy as np 

i = np.array([30, 45])  # A
io = i/(4 + 20)*4
vo = io*8

print(f"vo is {vo[0]:.4f} and {vo[1]:.4f} V, when is is 30 and 45 A, respectively.")
