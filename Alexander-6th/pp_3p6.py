# -16 + (i1 - i3)*4 + (i1 - i2)*2 = 0
# (i2 - i1)*2 + (i2 - i3)*8 - 10*i3 = 0
# i3*6 + (i3 - i2)*8 + (i3 - i1)*4 = 0
# ==>
# 6*i1 - 2*i2 - 4*i3 = 16
# -2*i1 + 10*i2 - 18*i3 = 0
# -4*i1 - 8*i2 + 18*i3 = 0

import numpy as np 

A = np.mat([[6, -2, -4], [-2, 10, -18], [-4, -8, 18]])
B = np.mat([16, 0, 0]).T

i = A.I*B

print(f"Io is {i[2, 0]:.4f} A.")