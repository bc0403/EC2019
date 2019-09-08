R1 = 12*6/(12 + 6)
R2 = 10*40/(10 + 40)
v = 30

v1 = v/(R1 + R2)*R1
v2 = v - v1
i1 = v1/12
i2 = v2/40
p1 = v1*i1
p2 = v2*i2

print(f"v1, i1, and p1 is {v1:.4f} V, {i1:.4f} A, and {p1:.4f} W, respectively.")
print(f"v2, i2, and p2 is {v2:.4f} V, {i2:.4f} A, and {p2:.4f} W, respectively.")