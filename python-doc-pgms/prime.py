def prime(n,k):
    print(k)
    for i in range(2,n):
        if(n%i==0):
            print("the number is not prime")
            break
    else:
        print("the number is prime")

if __name__ == "__main__":
    import sys
    prime(int(sys.argv[1]),int(sys.argv[2]))


