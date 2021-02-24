import re

rule = '[+]\d{2}\s[0-9]{10}'

var_name = input("Enter variable name")

matcher = re.fullmatch(rule, var_name)

if matcher is None:
    print("Invalid variable")
else:
    print("valid")
