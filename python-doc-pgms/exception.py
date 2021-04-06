while True:
    try:
        x=int(input("Enter"))
        print(x)
    except ValueError as ve:
        print("invalid number",ve)


