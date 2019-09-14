RN = 90
# short-circuit current, use KCL at two 90 ohm jiont node.
# (450 - v1)/90 + 4 = v1/90
v1 = (360 + 450)/2
IN = v1/90

print(f"RN and IN is {RN} ohm and {IN} A, respectively.")