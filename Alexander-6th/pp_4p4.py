# consider 5 A only
# vx/20 + vx/4 = 5 + 0.1*vx
vx_1 = 100/4

# consider 25 V only
# (25 - vx)/20 + 0.1*vx = vx/4
vx_2 = 25/4

vx = vx_1 + vx_2

print(f"vx is {vx:.4f} V.")