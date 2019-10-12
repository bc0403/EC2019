import numpy as np 

R = 100e3
L = 50e-3
C = 2e-9

omega0 = 1/np.sqrt(L*C)
Q = R/(omega0*L)
B = omega0/Q
omega1 = omega0 - B/2
omega2 = omega0 + B/2

print(f"omega0, omega1, omega2, Q, B:")
print(f"{omega0/1e3} krad/s, {omega1/1e3} krad/s, {omega2/1e3} krad/s, {Q}, {B/1e3} krad/s")