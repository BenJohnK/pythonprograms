import re

rule = '[a-k][369][a-zA-Z]*'

var_name = input("Enter variable name")

matcher = re.fullmatch(rule, var_name)

if matcher is None:
    print("Invalid variable")
else:
    print("valid")

