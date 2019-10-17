import numpy as np 
vs = 1
Rs = 1e6
RL = 10
print("If connected directly:")
print(f"voltage at the load: {vs*RL/(Rs + RL):.2e} V")
print(f"power at the load: {(vs*RL/(Rs + RL))**2/RL:.2e} W")

print("If a unity-gain buffer is used:")
vL = vs*0.5*0.5
pL = vL**2/RL
ps = 0.5*vs*vs/(2e6)
print(f"voltage at the load: {vL:.2e} V")
print(f"power at the load: {vL**2/RL:.2e} W")
print(f"voltage gain: {20*np.log10(0.25):.2f} dB")
print(f"power gain: {10*np.log10(pL/ps):.2f} dB")
  