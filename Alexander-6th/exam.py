# 10 = 2*i1 + 8*(i1 - i3)
# 6 = -(i1 - i3)*8 + i3*4

# 10*i1 - 8*i3 = 10
# -8*i1 + 12*i3 = 6

import numpy as np 

A = np.mat([[6, -1, 0], [2, -7, 1], [0, -1, 6]])
B = np.mat([3, 8, 2]).T

I = A.I*B

i1 = I[0, 0]
i2 = I[1, 0]
i3 = I[2, 0]

print(f"i1, i2, and i3 is {i1:.4f}, {i2:.4f}, and {i3:.4f} A, respectively.")