C1 = 20e-6
C2 = 30e-6

v1 = 50*0.9
v2 = 50*0.3

w1 = 0.5*C1*v1**2
w2 = 0.5*C2*v2**2

print(f"w1: {w1*1e3:.4f} mJ")
print(f"w2: {w2*1e3:.4f} mJ")