from bank_account import BankAccount

class User:
    
    def __init__(self, first, last, email, age):
        self.first = first
        self.last = last
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate = 0.06, balance = 3200)

    def display_info(self):
        print(self.first, self.last, self.email, self.age, self.is_rewards_member, self.gold_card_points)
        return self
        # print(self.last)
        # print(self.email)
        # print(self.age)
        # print(self.is_rewards_member)
        # print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print('You are already registered as a rewards member!')
        else:
            print('You have successfully registered for the rewards program!')
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
            print('You have spent ' + str(amount) + ' points, and you have ' + str(self.gold_card_points) + ' points remaining.')
        else:
            print('You do not have enough gold card points.')
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self
    
    def transfer_money(self, amount, other_user):
        self.account.withdraw(amount)
        print ('Money has been transferred to ' + str(other_user) + '.') # How do i get this to print the class instance name instead of the location?
        other_user.account.deposit(amount)
        return self

first_user = User('Troy', 'M.', 'tm@g', 33)

first_user.display_info()
first_user.enroll()
first_user.spend_points(50)
first_user.enroll()

second_user = User('Angelica', 'C.', 'ac@g', 24)

second_user.enroll()
second_user.spend_points(80)

third_user = User('Hannah', 'M.', 'hm@g', 22)
third_user.spend_points(80)

first_user.display_info()
second_user.display_info()
third_user.display_info()

# @classmethod                      ?
#     def display_all(cls):         ?
#         User.display_info()       ?

# first_user.display_info().enroll().enroll().spend_points(199).display_info()

first_user.make_deposit(100).display_user_balance()
second_user.display_user_balance()
third_user.make_withdrawal(100).display_user_balance()
first_user.transfer_money(1000, second_user).display_user_balance()
second_user.display_user_balance()
