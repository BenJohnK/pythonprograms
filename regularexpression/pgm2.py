# import re
#
# pattern="[abc]"
#
# matcher=re.finditer(pattern,"abc _ZK@7")
# for match in matcher:
#     print(match.start())
#     print(match.group())

import re

# pattern="[a-zA-Z]"
# pattern="[a-z]"
# pattern = "[A-Z]"
# pattern="[0-9]"
# pattern="[0-9a-zA-Z]"
# pattern="[^0-9a-zA-Z]"
# pattern="\s"
pattern="\d{2}"
# pattern="\D"
# pattern="\w"
# pattern= "\W"


matcher = re.finditer(pattern, "09abc _ZK@7")
for match in matcher:
    print(match.start())
    print(match.group())
