# create a supermesh by excluding 4A and 3 ohm
# -24 + (i1 - i3)*5 + (i2 - i3)*10 + i2*20 = 0
# (i3 - i1)*5 + i3*5 + (i3 - i2)*10 = 0
# 4 = i1 - i2
# ==>
# 5*i1 + 30*i2 - 15*i3 = 24
# -5*i1 - 10*i2 + 20*i3 = 0
#    i1 -    i2         = 4

import numpy as np 

A = np.mat([[5, 30, -15], [-5, -10, 20], [1, -1, 0]])
B = np.mat([24, 0, 4]).T

i = A.I*B

print(f"i1, i2, and i3 is {i[0, 0]:.4f}, {i[1, 0]:.4f}, and {i[2, 0]:.4f} A, respectively.")