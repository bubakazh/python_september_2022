class BankAccount:

    all_accounts = []
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.all_accounts.append(self.balance)
        
    def deposit(self, amount):
        self.balance += amount
        print('$' + str(amount) + ' has been deposited.')
        # print('Current balance: $' + str(self.balance))
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print('$' + str(amount) + ' has been withdrawn.')
            # print('Current balance: $' + str(self.balance))
        else:
            print('You have insufficient funds. A $5 fee will be charged to your account.')
            self.balance -= 5
            # print('Current balance: $' + str(self.balance))
        return self

    def display_account_info(self):
        print('Current balance: $' + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            print('Accrued interest: $' + str(self.balance * self.int_rate))
            self.balance = self.balance + self.balance * self.int_rate
            # print('Current balance: $' + str(self.balance))
        else:
            print('Your account is empty and cannot accrue any interest')
        return self

my_account = BankAccount(0.03, 1000)
her_account = BankAccount(0.05, 800)

my_account.deposit(100).deposit(200).deposit(300).withdraw(700).yield_interest().display_account_info()
her_account.deposit(1000).deposit(2000).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()

    # @classmethod
    # def print_bal(cls)
    #     print()

    # Will try to complete bonus at a later time.