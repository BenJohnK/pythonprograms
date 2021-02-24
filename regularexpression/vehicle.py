import re

rule = '[K][L][0-9]{2}[a-zA-Z]{2}[0-9]{4}'

var_name = input("Enter variable name")

matcher = re.fullmatch(rule, var_name)

if matcher is None:
    print("Invalid variable")
else:
    print("valid")

