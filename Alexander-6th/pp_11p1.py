import numpy as np 

# v(t) = 330*cos(10t + 20d)
# i(t) = 33*cos(10t - 30d)
# p(t) = 330*33*0.5*(cos(20t - 10d) + cos(50d))

Vm = 330
Im = 33
theta_v = 20
theta_i = -30
theta = theta_v - theta_i

p_avg = 0.5*Vm*Im*np.cos(theta/180*np.pi)
print(f"average power: {p_avg*1e-3:.2f} kW")
print(f"{330*33*0.5}")
