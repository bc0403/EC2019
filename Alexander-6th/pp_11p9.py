from cmath import *

Z = 60 + 40j
V = rect(155.56, 10/180*pi)

I = V/Z
S = 0.5*V*I.conjugate()
pf = S.real/abs(S)
if S.imag < 0:
    print(f"pf: {pf:.4f}, leading")
else:
    print(f"pf: {pf:.4f}, lagging")

print(f"apparent power: {abs(S):.4f} VA")