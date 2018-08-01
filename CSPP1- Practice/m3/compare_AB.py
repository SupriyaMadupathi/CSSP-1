'''
@author Supriyamadupathi
varA and varB, are assigned values,
either numbers or strings.
'''
VAR_A = 10
VAR_B = 8
if (isinstance(VAR_A, str) or isinstance(VAR_B, str)):
    print("string involved")
elif VAR_A > VAR_B:
    print("bigger")
elif VAR_A == VAR_B:
    print("equal")
else:
    print("smaller")
