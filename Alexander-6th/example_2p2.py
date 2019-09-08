v = 30  # V
R = 5e3  # ohm

i = v/R
G = 1/R
p = v*i

print(f"The current, conductance, and power is {i:.4f} A, {G:.4f} S, and {p:.4f} W, respectively.")