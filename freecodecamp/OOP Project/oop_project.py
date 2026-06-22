from bank_accounts import *

ahmad = BankAccount(1000, "Ahmad Ashfaq")

Asad = BankAccount(500, "Asadullah")

BankAccount.get_balance(Asad)
BankAccount.deposit(Asad, 1000) #Either you can call a function from a module like this.

ahmad.deposit(5000) #or this

ahmad.withdraw(6000)

ahmad.deposit(4000)
               
ahmad.transfer(1000, Asad)


ghanam = interestrewards(10000, "ghanam")

ghanam.deposits(1000)

ghanam.transfer(1000, ahmad)

arshad = SavingsAcct(5600, "Arshad")

arshad.withdraw(1000)