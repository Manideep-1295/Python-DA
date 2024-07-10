class LowBalanceError(Exception):
    def __init__(self,error):
        pass

class Bank:
    def __init__(self): 
        self.accounts = {}
    def accountNumber(self,num):
        if '91'+str(num) not in self.accounts:
            self.accounts['91'+str(num)] = 100
            print("HURRAY! Your account is updated with $100 as Welcome Bonus!!! Please Check Balance")
        else:
            print("User already registered !")
        return '91'+str(num)
    
    def deposit(self,amt,acc):
        if '91'+str(acc) not in self.accounts:
            print("Account does not exists!")
        else:
            self.accounts['91'+str(acc)] += amt
        return str(amt) + "$ Deposited Successfully"
    def withdraw(self,amt,acc):
        if '91'+str(acc) not in self.accounts:
            print("Account does not exists!")
        else:
            if amt > self.accounts['91'+str(acc)]:
                raise LowBalanceError("Insufficient Funds. Please deposit")
            else:
                self.accounts['91'+str(acc)] -= amt
                return str(amt) + "$ Withdrawn Successfully"
    def avblBal(self,num):
        return self.accounts['91'+str(num)]
    def users(self):
        return self.accounts
    def update(self):
        pass


user = Bank()
while True:
    term = int(input("Enter Your choice:\n \
                1. Create a New Account\n \
                2. Deposit Amount\n \
                3. Withdraw Amount\n \
                4. Check Balance\n \
                5. Update Balance\n \
                6. Exit\n \
                Enter your choice: "))

    match term:
        case 1:
            num = int(input("Enter your phone number: "))
            print("Your account number is : ",user.accountNumber(num))
        case 2:
            amt = int(input("Enter the amount you want to deposit: "))
            num = int(input("Enter your phone number: "))
            print(user.deposit(amt,num))
        case 3:
            try:
                amt = int(input("Enter the amount you want to withdraw: "))
                num = int(input("Enter your phone number: "))
                print(user.withdraw(amt,num))
            except LowBalanceError as lbe:
                print(lbe)
        case 4:
                num = int(input("Enter your phone number: "))
                print("Available Balance is: ",user.avblBal(num))
        case 5:
            pass
        case 6:
            exit()
        case 7:
            print(user.users())
        case _:
            print("Invalid input, choose correctly")
            
