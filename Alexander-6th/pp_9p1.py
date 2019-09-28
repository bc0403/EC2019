from cmath import *

Vm = 45
omega = 5*pi
phase = 36
T = 2*pi/omega
f = 1/T

print(f"{Vm}, {phase} degree, {omega:.4f} rad/s, {T*1e3} ms, {f} Hz")