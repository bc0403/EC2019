from cmath import *
import numpy as np 

# equivalent T network
# ===2j=======3j===
#         ||       
#         3j
#         ||
# =================
#
# -12 + I1*(-4j + 2j + 3j) - I2*(3j) = 0
# I2*(3j + 3j + 12) - I1*3j = 0
#
A = np.mat([[1j, -3j], [-3j, 12 + 6j]])
B = np.mat([12, 0]).T
I = A.I*B
I1 = I[0, 0]
I2 = I[1, 0] 
print(f"I1: {abs(I1):.4f}, {phase(I1)/pi*180:.4f}")
print(f"I1: {abs(I2):.4f}, {phase(I2)/pi*180:.4f}")