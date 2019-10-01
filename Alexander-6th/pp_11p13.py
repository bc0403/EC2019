from cmath import *

VR = sqrt(240*60)
I1 = VR/60
V1 = I1*(60 + 20j)
I2 = V1/(30 - 10j)
I = I1 + I2
V = I*20 + V1

print(f"V: {abs(V):.4f}, {phase(V)/pi*180:.4f} V")

S1 = (I*20)*I.conjugate()
S2 = V1*I2.conjugate()
S3 = V1*I1.conjugate()

print(f"for 20 ohm resistor, complex power: {S1:.4f} VA")
print(f"for 30 - 10j resistor, complex power: {S2:.4f} VA")
print(f"for 60 + 20j resistor, complex power: {S3:.4f} VA")
print(f"all: {S1 + S2 + S3:.4f} VA")
print(f"should be zero: {V*I.conjugate() - S1 - S2 - S3:.4f}")
