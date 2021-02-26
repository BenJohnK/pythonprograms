import re

rule = '\w+[@][g][m][a][i][l][.][c][o][m]'

var_name = input("Enter variable name")

matcher = re.fullmatch(rule, var_name)

if matcher is None:
    print("Invalid variable")
else:
    print("valid")
