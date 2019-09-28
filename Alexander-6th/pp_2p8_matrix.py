# 10 = 2*i1 + 8*(i1 - i3)
# 6 = -(i1 - i3)*8 + i3*4

# 10*i1 - 8*i3 = 10
# -8*i1 + 12*i3 = 6

import numpy as np 

A = np.mat([[10, -8], [-8, 12]])
B = np.mat([10, 6]).T

I = A.I*B

i1 = I[0, 0]
i3 = I[1, 0]
i2 = i1 - i3
v1 = i1*2
v2 = i2*8
v3 = i3*4

print(f"v1, v2, and v3 is {v1:.4f}, {v2:.4f}, and {v3:.4f} V, respectively.")
print(f"i1, i2, and i3 is {i1:.4f}, {i2:.4f}, and {i3:.4f} A, respectively.")