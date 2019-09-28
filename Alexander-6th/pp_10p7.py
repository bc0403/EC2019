from cmath import *

# step 1, "Is and 4-3j" to "vs + zs"
Is = rect(2.4, pi/2)
Zs = 4 - 3j
Vs = Is*Zs

# step 2
Zs_2 = Zs + 2 + 1j
Is_2 = Vs/Zs_2

# step 3
Zs_3 = Zs_2*5j/(Zs_2 + 5j)
Io = Is_2/(Zs_3 + 1 - 2j)*Zs_3

print(f"{abs(Io):.4f}, {phase(Io)/pi*180:.4f}")

