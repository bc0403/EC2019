# -90 + i1*6 + (i1 - i2)*10 + i1*4 = 0
# (i2 - i1)*10 + i2*15 + 40 + i2*5 = 0
# ==>
# 20*i1 - 10*i2 = 90
# -10*i1 + 30*i2 = -40

import numpy as np 

A = np.mat([[20, -10], [-10, 30]])
B = np.mat([90, -40]).T

i = A.I*B

print(f"i1 and i2 is {i[0, 0]:.4f} and {i[1, 0]:.4f} A, respectively")