class User:
    def __init__(self, first, last, age, email):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.Checking_Account = BankAccount(0.0275, 25000)
        self.Savings_Account = BankAccount(0.0475, 100000)
    def make_deposit(self, amount):
        self.Checking_Account.deposit(amount)
        self.Savings_Account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.Checking_Account.withdraw(amount)
        self.Savings_Account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.Checking_Account.display_account_info()
        self.Savings_Account.display_account_info()
        return self
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount): #deposit method increases account balance
        self.balance += amount
        print(f"You deposited ${amount:,.2f}, your balance is now: ${self.balance:,.2f}")
        return self
    def withdraw(self,amount): #withdraw method decrease account balance
        if amount < self.balance:
            self.balance -= amount
            print(f"You withdrew ${amount:,.2f}, your balance is now: ${self.balance:,.2f}")
        else:
            self.balance -= 5 #you get charged a $5 fee if there are insufficient funds in your account
            print(f"insufficient funds: Charging a $5 fee.  Your balance is now: ${self.balance:,.2f}")
        return self
    def display_account_info(self): #this will display your current balance
        print(f"Your current balance is: ${self.balance:,.2f}")
        return self
    def yield_interest(self): #this method yields interest depending on your account interest rate
        interest_earned = self.int_rate * self.balance
        self.balance += interest_earned
        print(f"Congratulations!  You earned ${interest_earned:,.2f} in interest.  Your current balance is: ${self.balance:,.2f}.")
        return self
    @classmethod
    def all_account_info(cls): #class method prints account info for both accounts
        print(f"Checking Account: Balance: ${Checking_Account.balance:,.2f}, Interest Rate: {Checking_Account.int_rate}")
        print(f"Savings Account: Balance: ${Savings_Account.balance:,.2f}, Interest Rate: {Savings_Account.int_rate}")


Checking_Account = BankAccount(0.0275, 25000) #created 2 new accounts
Savings_Account = BankAccount(0.0475, 100000)

user_Matt = User("Matt", "Cope", 39, "matthew.p.cope@gmail.com") #new user instances created
user_Jen = User("Jan", "Banzian", 41, "janbanzian@gmail.com") 
user_Mark = User("Mark", "Smith", 40, "msmith@gmail.com")
user_Matt.Checking_Account.make_deposit(500)
print(user_Matt.Checking_Account.balance)
print(user_Matt.Savings_Account.balance)