# calculate the Thevenin's theorem equivalent circuit
# set current io, find vo
# -vx/60 + (-vx - 3vx)/30 = io
# vo = -vx + 120*io
# ==> 9vx = -60*io
# ==> vo = (20/3 + 120)*io
RTh = 20/3 + 120

# open-circuit voltage
# -9 + vx + i*30 + 3vx = 0
# vx = i*60
i = 9/270
VTh = 9 - i*60
pmax = (VTh/2)**2/RTh

print(f"The maximum power is {pmax:.4f} W when RL equals {RTh:.4f} ohm.")