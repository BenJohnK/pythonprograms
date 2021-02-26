import re

# pattern="a*"
pattern="a+"
# pattern="a{2,3}"
count=0
matcher=re.finditer(pattern,"aaaabababab")
print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
# print(count)
