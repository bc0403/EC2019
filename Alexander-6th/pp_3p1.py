# 14 = v1/4 + (v1 - v2)/5
# (v1 - v2)/5 = v2/5 + 7
# ==>
# 9*v1 - 4*v2 = 280
# v1 - 2*v2 = 35

import numpy as np 

A = np.mat([[9, -4], [1, -2]])
B = np.mat([280, 35]).T

v = A.I*B

print(f"v1 and v2 is {v[0, 0]:.4f} and {v[1, 0]:.4f} V, respectively.")
