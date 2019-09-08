v = 20  # V
R1 = 2  # ohm
R2 = 3  # ohm

i = v/(R1 + R2)
v1 = i*R1
v2 = -i*R2

print(f"voltage v1 and v2 is {v1:.4f} and {v2:.4f} V, respectively. ")