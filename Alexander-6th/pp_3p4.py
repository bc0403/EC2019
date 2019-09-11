# enclose two voltage source and the parallel 6 ohm resistor as supernode
# v1/2 + v2/4 + v3/3 = 0
# v2 = v1 - 25
# v3 - v2 = 5*(v1/2)
# ==>
# 6*v1 + 3*v2 + 4*v3 = 0
#   v1 -   v2        = 25
# 5*v1 + 2*v2 - 2*v3 = 0

import numpy as np 

A = np.mat([[6, 3, 4], [1, -1, 0], [5, 2, -2]])
B = np.mat([0, 25, 0]).T

v = A.I*B
print(f"v1, v2, and v3 is {v[0, 0]:.4f}, {v[1, 0]:.4f}, and {v[2, 0]:.4f} V, respectively.")