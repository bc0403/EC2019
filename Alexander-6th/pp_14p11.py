import numpy as np 

omega0 = 2*np.pi*20.2e3
B = 2*np.pi*0.2e3
R = 30e3

Q = omega0/B
L = Q*R/omega0
C = 1/(omega0**2*L)

print(f"L, C, and Q: {L} H, {C*1e12} pF, and {Q}")
