from cmath import *
import numpy as np 

# open circuit voltage
# v1/(4 - 2j) + 8 + (v1 - v2)/(8 + 4j) = 0
# 8 + (v1 - v2)/(8 + 4j) + 0.2*(v1 - v2) = 0
# ==>
# (1/(4 - 2j) + 1/(8 + 4j))*v1 - 1/(8 + 4j)*v2 = -8
# (1/(8 + 4j) + 0.2)*v1 - (1/(8 + 4j) + 0.2)*v2 = -8
A = np.mat([
    [1/(4 - 2j) + 1/(8 + 4j), -1/(8 + 4j)], 
    [1/(8 + 4j) + 0.2, -1/(8 + 4j) - 0.2]])
B = np.mat([-8, -8]).T
V = A.I*B
print(f"Vth: {abs(V[1, 0]):.4f}, {phase(V[1, 0])/pi*180:.4f}")

# Zth, turn off independent source, keep dependent source
# apply 1 A current source
# (1 + 0.2*Vo)*(12 + 2j) = Vx
# Vo = -(1 + 0.2*Vo)*(8 + 4j)
Vo = -(8 + 4j)/(1 + 0.2*(8 + 4j))
Vx = (1 + 0.2*Vo)*(12 + 2j) 
print(f"Zth: {abs(Vx):.4f}, {phase(Vx)/pi*180:.4f}")

