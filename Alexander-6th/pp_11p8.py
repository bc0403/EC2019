from sympy import *

t = symbols("t")
v = abs(100*sin(t))
v_rms = sqrt(1/pi*integrate(v**2, (t, 0, pi)))

p = v_rms.evalf()**2/6

print(f"rms value: {v_rms.evalf():.4f} V")
print(f"power dissipated in 6 ohm resistor: {p:.4f} W")