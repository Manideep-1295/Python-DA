class LowBalanceError(Exception):
    def __init__(self,error):
        pass

class NegativeNumberError(Exception):
    def __init__(self,error):
        pass

class AccountNumberLengthError(Exception):
    def __init__(self,error):
        pass

class InvalidInput(Exception):
    def __init__(self,error):
        pass


class Bank:
    def __init__(self): 
        self.accounts = {}
    def accountNumber(self,num):
        if len(num) != 10 and int(num[0]) < 6: 
            raise AccountNumberLengthError("Given phone number is invalid")
        else:
            if '91'+str(num) not in self.accounts:
                self.accounts['91'+str(num)] = 100
                print(f"HURRAY! Your account - {'91'+str(num)} is updated with $100 as Welcome Bonus!!! Please Check Balance")
            else:
                print("User already registered !")
            return '91'+str(num)
    
    def deposit(self,amt,acc):
        if amt <= 0:
            raise NegativeNumberError("Negative number not allowed in deposits!")
        elif int(acc[0]) < 6 and len(acc) != 10:
            raise AccountNumberLengthError("Account number invalid!")
        else:
            if '91'+str(acc) not in self.accounts:
                print("Account does not exists!")
            else:
                self.accounts['91'+str(acc)] += amt
                return str(amt) + "$ Deposited Successfully"
    def withdraw(self,amt,acc):
        if amt <= 0:
            raise NegativeNumberError("Negative number not allowed in deposits!")
        elif int(acc[0]) < 6 and len(acc) != 10:
            raise AccountNumberLengthError("Account number invalid!")
        else:
            if '91'+str(acc) not in self.accounts:
                print("Account does not exists!")
            else:
                if amt > self.accounts['91'+str(acc)]:
                    raise LowBalanceError("Insufficient Funds. Please deposit")
                else:
                    self.accounts['91'+str(acc)] -= amt
                    return str(amt) + "$ Withdrawn Successfully"
    def avblBal(self,num):
        if len(num) != 10 and int(num[0]) < 6: 
            raise AccountNumberLengthError("Given phone number is invalid")
        else:
            return self.accounts['91'+str(num)]
    def users(self):
        return self.accounts
    def update(self):
        print(f"Updated Balance: {self.accounts['91'+str(num)]}")


try:
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
                try:
                    num = input("Enter your phone number: ")
                    print("Your account number is : ",user.accountNumber(num))
                except AccountNumberLengthError as anle:
                    print(anle)
            case 2:
                try:
                    amt = int(input("Enter the amount you want to deposit: "))
                    num = input("Enter your phone number: ")
                    print(user.deposit(amt,num))
                except NegativeNumberError as nne:
                    print(nne)
                except Exception as e:
                    print(e)
            case 3:
                try:
                    amt = int(input("Enter the amount you want to withdraw: "))
                    num = input("Enter your phone number: ")
                    print(user.withdraw(amt,num))
                except LowBalanceError as lbe:
                    print(lbe)
                except Exception as e:
                    print(e)
            case 4:
                    try:
                        num = input("Enter your phone number: ")
                        print("Available Balance is: ",user.avblBal(num))
                    except AccountNumberLengthError as anle:
                        print(anle)
            case 5:
                user.update()
            case 6:
                exit()
            case 7:
                print(user.users())
            case _:
                print("Invalid input, choose correctly")
except InvalidInput as ii:
    print(ii)
