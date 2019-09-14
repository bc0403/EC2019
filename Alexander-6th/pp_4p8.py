# turn off independent sources
Rth = 180*60/(180 + 60)

# open-circuit voltage, name the joint node of 90 ohm, 90 ohm, and 2A as node 1
# (180 - v1)/90 + 2 = v1/150
# ==> 
# 180*5 - 5*v1 + 900 = 3*v1
v1 = (180*5 + 900)/8
Vth = v1/150*60

I = Vth/(Rth + 15)

print(f"Vth, Rth, and I is {Vth:.4f} V, {Rth:.4f} ohm, and {I:.4f} A, respectively")
