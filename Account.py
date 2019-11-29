import pickle
class Account(object):
    nextAccountNumber = 123456
    def __init__(self, name:str, balance:int):
            self.__accountNumber = Account.nextAccountNumber
            Account.nextAccountNumber += 1
            self.__name = name
            self.__balance = balance

    def getAccountNumber(self):
            AccountNumber = self.__accountNumber
            return AccountNumber

    def getName(self):
            customerName = self.__name
            return customerName

    def getBalance(self):
            customerBalance =  self.__balance
            return customerBalance

    def deposit(self, amount:float):
            self.__balance += amount

    def withdraw(self, amount:float):
            if self.__balance >= amount:
                self.__balance -= amount
                return True
            else:
                return False

    def displayAccount(self):
            return "Name: {}\nAccount Number: {}\nBalance: {}".format(self.__name, self.__accountNumber, self.__balance)


class CheckingAccount(Account):
    interestRate = 0.0125
    minimumBalance = 500.00

    def __init__(self, name:str, balance:int):
            super().__init__(name, balance)

    def withdraw(self, amount:float):
            if ((self.getBalance() - amount) < CheckingAccount.minimumBalance) and ((self.getBalance() - 10) - amount) > 0:
                super().withdraw(amount + 10)
                return True


            elif (self.getBalance() - amount >= CheckingAccount.minimumBalance):
                super().withdraw(amount)
                return True
            else:
                return False

    def depositInterest(self):
            interestEarned = (self.getBalance() * CheckingAccount.interestRate)
            super().deposit(round(interestEarned, 2))

    def displayAccount(self):
            display = "Name: {}\nAccount Number: {}\nBalance: {}\nInterest Rate: {}%".format(self.getName(), self.getAccountNumber(), self.getBalance(), (CheckingAccount.interestRate *100))
            return display
class Bank(object):
    def __init__(self):
        self.__accounts = self.__generateAccounts()
        account = self.__accounts[-1]
        lastAccountNumber = account.getAccountNumber()
        Account.nextAccountNumber = int(lastAccountNumber) + 1


    def addAccount(self, checking:bool):
        name = str(input("Enter a name: "))
        balance = float(input("Enter an account Balance: "))
        if checking:
             account = CheckingAccount(name, balance)
        else:
            account = Account(name, balance)
        self.__accounts.append(account)

    def displayAccounts(self):
        for i in self.__accounts:
            print(i.displayAccount(), "\n")
    def findAccount(self, number):
        for i in self.__accounts:
            objNum = i.getAccountNumber()
            if objNum == number:
                return i
        return None
    def removeAccount(self, number):
        for i in self.__accounts:
            objNum = i.getAccountNumber()
            if objNum == number:
                self.__accounts.remove(i)
                return True
        return False
    def __generateAccounts(self):
        f = open("BankAccountFile.dat", "rb")
        try:
            list = pickle.load(f)
            f.close()
            return list
        except:
            f.close()
            return []

    def writeToFile(self):
        f = open("BankAccountFile.dat", "wb")
        pickle.dump(self.__accounts, f)
        f.close()


















