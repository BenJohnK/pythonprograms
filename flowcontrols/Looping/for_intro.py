for i in range(0,10,2):
    print(i, end="")
for i in range(10,2,-1):
    print(i)

# limit=int(input("Enter limit"))
#
# for i in range(limit):
#     if i % 2 == 0:
#         print(i)


lowlimit=int(input("Enter lower limit"))
upperlimit=int(input("Enter upper limit"))

for i in range(lowlimit, upperlimit):
    if i % 2 == 0:
        print(i)

