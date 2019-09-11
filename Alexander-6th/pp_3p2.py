# 4 = (v1 - v2)/3 + (v1 - v3)/2
# (v1 - v2)/3 + 4*(v2/4) = v2/4
# (v1 - v3)/2 = 4*(v2/4) + v3/6
# ==>
# 5*v1 - 2*v2 - 3*v3 = 24
# 4*v1 + 5*v2       = 0
# 3*v1 - 6*v2 - 4*v3 = 0

import numpy as np 

A = np.mat([[5, -2, -3], [4, 5, 0], [3, -6, -4]])
B = np.mat([24, 0, 0]).T

v = A.I*B

print(f"v1, v2, and v3 is {v[0, 0]:.4f}, {v[1, 0]:.4f}, and {v[2, 0]:.4f} V, respectively.")