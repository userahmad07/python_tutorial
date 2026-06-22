class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance, accname):
        self.balance = initial_balance
        self.name = accname
        print(
            f"\nAccount: {self.name} created. \n balance = ${self.balance} \n****************") #When you run the program this print statement will get executed because it's a function even though it's inside a class.
    
    def get_balance(self):
        print(f"\n{self.name}'s balance is ${self.balance}") 
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit of {amount} Successful!\n{self.name}'s balance is ${self.balance} \n****************")
    
    def viable_transaction(self, amount):
        if self.balance >= amount :
            return
        else:
            raise BalanceException(
                f"\n Not enough balance in {self.name}'s account"
                )
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)  #We wrote a withdraw function and inside it called viable transaction function that has the logic to check the balance and transaction amount. without this line the function can't run in itself
            self.balance = self.balance - amount
            print(f"\nWithdrawal Transaction completed you current balance is {self.balance}")

        except BalanceException as error:
            print(f"Withdraw Interupted: {error}")

    def transfer(self, amount, recipient):
        try:
            print("\n****************\n\nBeginning Transfer")
            self.viable_transaction(amount)
            self.withdraw(amount)
            recipient.deposit(amount)
            print(f"\nTransfer Completed!!! {amount} has been transferred")
        except BalanceException as error:
            print(f"Transfer Interupted: {error}")
class interestrewards(BankAccount):
    def deposits(self, amount):
        self.balance = self.balance + amount * 1.05
        print("Deposit Completed")
        self.get_balance()

class SavingsAcct(interestrewards):
    def __init__(self, initial_balance, accname):
        super().__init__(initial_balance, accname)
        self.fee = 5     #At first I thought why inherit things as we're not even adding new fields, but we had to add a fee field and without editing the init method we could not do that, and so we also used super() with same parameters. Just so we can add that fee field
    
    def withdraw(self, amount):
        self.viable_transaction(amount + self.fee)
        self.balance = self.balance - amount - self.fee
        print("Withdrawal Completed")
        self.get_balance()