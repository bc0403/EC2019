import numpy as np 

# A*v == B
A = np.mat([[3, -2, -1],
            [-4, 7, -1],
            [2, -3, 1]])

B = np.mat([12, 0, 0]).T

v = A.I*B

print(f"v1 = {v[0, 0]:.4f} V; v2 = {v[1, 0]:.4f} V; v3 = {v[2, 0]:.4f} V.")