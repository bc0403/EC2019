from cmath import *
# v(t) = -25*cos(omega*t + 40d) = 25*cos(omega*t - 140d)

I = 1j*(12 - 5*1j)
print(f"{abs(I)}, {phase(I)/pi*180:.4f}")