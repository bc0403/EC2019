# set the bottom node as reference ground;
# enclose the 6V voltage source as a supernode;
# name the "-" node of 6V as node 1;
# name the "+" node of 6V as node 2.
#  
# (14 - v1)/4 = v1/3 + v2/2 + v2/6
# v2 = v1 + 6
# ==>
# 7*v1 + 8*v2 = 14*3
#  -v1 +   v2 = 6

import numpy as np 

A = np.mat([[7, 8], [-1, 1]])
B = np.mat([42, 6]).T

v = A.I*B
i = v[1, 0]/2
print(f"the v an i in figure is {v[0, 0]:.4f} V and {i:.4f} A, respectively.")