class AgeError(Exception):
    pass

class AccnoError(Exception):
    pass

class AcctypeError(Exception):
    pass

class Bank:
    def __init__(self, name, age, accno, acctype, balance):
        self.name = name
        self.age = age
        self.accno = accno
        self.acctype = acctype
        self.balance = balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance=self.balance-amount
        else:
            print("Invalid Balance")

    def display(self):
        print(" name ", self.name, "\n", "acc-no", self.accno, "\n", "age ",
              self.age, "\n", "acc-type ", self.acctype, "\n", "balance ", self.balance)

accounts = []

flag =0
while (flag == 0):
    print("\nMenu:")
    print("1. Create a new account")
    print("2. Deposit to an account")
    print("3. Withdraw from an account")
    print("4. Print account details")
    print("5. Exit")
    ch = int(input("Enter your choice"))
    if ch == 1:
        name = str(input("Enter the name: "))
        age = int(input("Enter age: "))
        try:
            if (age < 18 or age > 100):
                raise AgeError
        except AgeError:
            print("Age should between 18 to 100")
            exit()
            
        accno = (input("Enter accno: "))
        try:
            if (len(accno) < 5):
                raise AccnoError
        except AccnoError:
            print("Account no should be more than 5 digits")
            exit()
        acctype = (input("Enter acctype: "))
        try:
            if (acctype not in ['S','C']):
                raise AcctypeError
        except AcctypeError:
            print("Acc type should be C or S")
            exit()
        balance = int(input("Enter the Balance: "))
        B1 = Bank(name, age, accno, acctype, balance)
        accounts.append(B1)
        print(accounts)
    if ch == 2:
        acc_no = int(input("Enter accNo: "))
        amountDep = input("Enter amount to for deposit")
        for acc in accounts: 
            if acc_no == int(acc.accno):
                acc.deposit(amountDep)
    if ch == 3:
        acc_no = int(input("Enter accNo: "))
        amountWith = input("Enter amount to withdraw")
        for acc in accounts: 
            if acc_no == int(acc.accno):
                acc.withdraw(amountWith)
    if ch == 4:
        acc_no = int(input("Enter accNo: "))
        for account in accounts:
            print(account.accno)
            if acc_no == int(account.accno):
                account.display()
            else:
                print("account not found!")
    if ch == 5:
        print("Exiting")
        flag = 1
