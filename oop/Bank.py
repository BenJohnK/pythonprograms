class Bank:
    bank_name = "SBI"

    def __init__(self, accno, pname, minbal):
        self.accno = accno
        self.pname = pname
        self.balance = minbal

    def deposit(self, amount):
        self.balance += amount
        print("Account Credited with: ", amount, "Balance: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("No sufficient funds")
        else:
            self.balance -= amount
            print("Account debited with: ", amount, "Balance: ", self.balance)


obj = Bank(1000,"Ben",3000)
obj.deposit(3000)
obj.withdraw(6000)

# i = 0
# lst = []
# n = int(input("Enter number of accounts you need to create"))
# while i < 5:
#     lst.append(Bank())
#     i = i + 1
# print(lst)
# print(Bank.bank_name)
# print(obj.bank_name)
# obj.bank_name="Federal"
# print(obj.bank_name)
# obj1=Bank()
# print(obj1.bank_name)

# Bank.bank_name="Federal"
# print(obj.bank_name)
# obj2=Bank()
# print(obj2.bank_name)

