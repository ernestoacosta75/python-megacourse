'''
This class represents a bank account.

@author Ernesto Antonio Rodriguez Acosta
'''
class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance = int(file.read())

        print('Initial balance: ' + str(self.balance))

    '''
        Updates the account balance according to the ammount to withdraw.
    '''
    def withdraw(self, amount):
        if(amount > self.balance):
            pass
        else:
            self.balance = self.balance - amount
            self.update_balance()

    '''
        Updates the account balance according to the ammount to be deposited.
    '''
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.update_balance()


    def update_balance(self):
        with open(self.filepath, 'r+') as file:
            file.write(str(self.balance))
            file.seek(0)

            print('Actual balance: ' + file.read())

bank_account = Account('balance.txt')

#bank_account.withdraw(100)

bank_account.deposit(100)
