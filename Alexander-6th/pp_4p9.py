# turn off the independent source, set vab = vo
# (vo + ix*3)/5 = 0.5*ix
# ==> ix = -2*vo
# io + ix = vo/4
# ==> io = 2.25 vo
Rth = 1/2.25

# open-circuit voltage
# 7*ix = 6 + 0.5ix*5
ix = 6/4.5
Vth = ix*4

print(f"Vth and Rth is {Vth:.4f} V and {Rth:.4f} ohm, respectively.")




