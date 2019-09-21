from cmath import sqrt

R = 10
L = 5
C = 2e-3

alpha = R/(2*L)
omega0 = 1/sqrt(L*C)
s1 = -1*alpha + sqrt(alpha**2 - omega0**2)
s2 = -1*alpha - sqrt(alpha**2 - omega0**2)

print(f"alpha, omega0, s1, s2 is {alpha}, {omega0}, {s1:.3f}, {s2:.3f}, respectively.")