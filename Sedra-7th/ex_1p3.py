import numpy as np 

vs = 10e-3
Rs = 1e3
RL = np.array([100e3, 10e3, 1e3, 100])

# vo = vs*(RL)/(Rs + RL)
vo = vs*RL/(RL + Rs)
print(vo)

# RL/(RL + Rs) = 0.8
RL_min = 0.8*Rs/0.2
print(RL_min)