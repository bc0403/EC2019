R1 = 9 + 3  # kohm
R2 = 15*60/(15 + 60)
i = 30  # mA

i1 = i/(R1 + R2)*R2 
i2 = (i - i1)/(15 + 60)*15
v1 = i1*9  # V
v2 = i2*60
p1 = v1*i1  # mW
p2 = v2*i2
ps = v2*i

print(f"v1 and v2 is {v1:.4f} and {v2:.4f} V, respectively.")
print(f"p1 and p2 is {p1:.4f} and {p2:.4f} mW, respectively.")
print(f"power supplied by the current source is {ps:.4f} mW")