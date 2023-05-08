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
Checking_Account.deposit(500).deposit(6000).deposit(3000).withdraw(5000).yield_interest().display_account_info()
Savings_Account.deposit(7000).deposit(8000).withdraw(9000).withdraw(500).withdraw(2000).yield_interest().display_account_info()
BankAccount.all_account_info() # prints info for all accounts
