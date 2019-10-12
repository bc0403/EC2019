R = 4
L = 25e-3
Q = 50

# Q = omega0*L/R
omega0 = Q*R/L

# omega0 = 1/sqrt(L*C)
C = 1/(omega0**2*L)

print(f"C: {C*1e6:.3f} uF")

# Q = omega0/B
B = omega0/Q
omega1 = omega0 - B/2
omega2 = omega0 + B/2
print(f"omega1: {omega1} rad/s")
print(f"omega2: {omega2} rad/s")
print(f"B: {B} rad/s")

I = 100/4
Pmax = 0.5*I**2*R
print(f"power dissipated at omega0, omega1, and omega2 are {Pmax}, {Pmax/2}, and {Pmax/2} W")