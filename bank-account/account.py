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

class CheckingAccount(Account):
    """This class generates checking account objects."""

    type = "checking"

    def __init__(self, filepath, fee):
        super().__init__(filepath)
        self.fee = fee

    '''
        To transfer an amount of money.
    '''
    def transfer(self, amount):
        if(amount > self.balance):
            pass
        else:
            self.balance = self.balance - amount - self.fee
            self.update_balance()

jack_checking = CheckingAccount('balance.txt', 1)
#checking.deposit(10)
jack_checking.transfer(110)
print(jack_checking.__doc__)