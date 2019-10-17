import numpy as np 

# 1/RC = 2pi*100 Hz
R = 10e3
C = 1/(2*np.pi*100*R)
print(f"C: {C*1e6:.2f} uF")