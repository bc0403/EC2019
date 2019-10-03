# mark the red dot terminal as "+", and all the mesh current clockwise
# -240 + 4*I1 + V1 = 0
# V2 + I2*10 - I3*2 = 0
# -V1 + 10*I3 - 2*I2 - V2 = 0
# V2 = 2*V1
# I2 - I3 = -0.5*(I1 - I3)
# ==>
import numpy as np 

# find V1, I1, V2, I2, I3
A = np.mat([
    [1, 4, 0, 0, 0],
    [0, 0, 1, 10, -2],
    [-1, 0, -1, -2, 10],
    [2, 0, -1, 0, 0],
    [0, 0.5, 0, 1, -1.5]
])
B = np.mat([240, 0, 0, 0, 0]).T
v = A.I*B
I3 = v[4, 0]
Vo = I3*8

print(f"Vo: {Vo:.4f} V")