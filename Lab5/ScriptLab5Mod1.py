# a.	Create a class called CheckingAccountBalance.  Create an initial variable (StartingAmount) and set it equal to $1k.  Within the Class you will create 2 Methods
#   i.	Method1 (deposit) will accept one value
#       1.	User will be asked how much they would like to deposit
#       2.	Once user enters amount, that amount is added to their Balance
#       3.	Print the new balance
#   ii.	Method2 (withdrawal) will accept one value
#       1.	User will be asked how much they would like to withdraw
#       2.	Once user enters amount, that amount is deducted from their Balance
#       3.	Print the new balance
from pip._vendor.distlib.compat import raw_input


class CheckingAccountBalance:
    balance = 1000.00

    def CheckingAccountBalance(self):
        self.balance = 1000.00

    def deposit(self):
        depositValue = raw_input('How much would you like to Deposit?\n')
        self.balance += float(depositValue)
        print('Deposited: %f \nCurrent Balance: %f' % (float(depositValue), self.balance))

    def withdrawal(self):
        withdrawalAmt = raw_input("How much Would you like to Withdraw?\n")
        self.balance -= float(withdrawalAmt)
        print('Withdrawal: %f \nCurrent Balance: %f\n' % (float(withdrawalAmt), self.balance))
