# the current of the controlled current source should be i_0/3, not i_o

# io + io/3 + io*2/12 = 15
io = 15*6/(1 + 2 + 6)
vo = io*2

print(f"vo and io is {vo:.4f} V and {io:.4f} A, respectively.")