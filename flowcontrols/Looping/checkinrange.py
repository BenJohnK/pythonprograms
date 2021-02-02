power = int(input("Enter power"))
low_lim = int(input("Enter lower limit"))
up_lim = int(input("Enter upper limit"))
cutoff = (low_lim+up_lim)//2
res = 1
for i in range(1, cutoff):
    res = i**power
    for j in range(low_lim, up_lim+1):
        if res == j:
            print(res)









