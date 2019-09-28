from cmath import *

omega = 10
zL = 1j*omega*0.5
zC = 1/(1j*omega*(1/20))
z1 = zL*10/(zL + 10)
vs = rect(50, 30/180*pi)
vo = vs/(z1 + zC)*zC
print(f"{abs(vo):.4f}, {phase(vo)/pi*180:.4f}")