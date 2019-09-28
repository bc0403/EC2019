from cmath import *
import numpy as np 

# -60 + (15 - 4j)*I1 - (-4j)*I2 - 5*I3 = 0
# 5*I3 + (-4j)*I2 + 8j*I2 + (-6j)*I3 - (5-4j)*I1 = 0
# I3 - I2 = 2.4
# ==>
# (15 - 4j)*I1 + 4j*I2 - 5*I3 = 60
# -(5 - 4j)*I1 + 4j*I2 + (5 - 6j)*I3 = 0
#                  -I2 +          I3 = 2.4

A = np.mat([[15 - 4j, 4j, -5], [-5 + 4j, 4j, 5 - 6j], [0, -1, 1]])
B = np.mat([60, 0, 2.4]).T
I = A.I*B

print(f"{abs(I[0, 0]):.4f}, {phase(I[0, 0])/pi*180:.4f}")