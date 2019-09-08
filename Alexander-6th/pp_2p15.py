# change the right wye to delta
R1 = 40
R2 = 20
R3 = 100

Rsum = R1*R2 + R2*R3 + R3*R1
Ra = Rsum/R1
Rb = Rsum/R2
Rc = Rsum/R3

Rx = Rc*48/(Rc + 48) + Rb*60/(Rb + 60)
Ry = Rx*Ra/(Rx + Ra)
Rab = Ry + 6
v = 240
i = v/Rab

print(f"Rab and i is {Rab:.4f} ohm and {i:.4f} A, respectively.")