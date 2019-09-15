C34 = 60*30/90
C2 = C34 + 20
Ceq = C2*40/(C2 + 40)
Q = Ceq*1e-6*150

v1 = Q/40e-6
v2 = 150 - v1
v3 = v2/90*30
v4 = v2/90*60

print(f"v1, v2, v3, v4 is {v1:.1f}, {v2:.1f}, {v3:.1f}, and {v4:.1f} V, respectively.")