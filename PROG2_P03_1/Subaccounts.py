from Bankaccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, bank_account: str, account_balance: float=0.0, currency:str= "CHF", monthly_interest: float=0.001):
        super().__init__(bank_account, account_balance, currency)
        self.monthly_interest = monthly_interest # 0.1% = 0.001

    def set_monthly_interest(self, interest):
        self.monthly_interest = interest

    def interest(self):
        # calculate interest: account_balance * monthly interest
        interest_monthly = self.account_balance * self.monthly_interest
        return interest_monthly

    def withdraw(self, amount: float=0.0): # Geld abheben
        charge = 0.02 # 2% = 0.02
        if not self.is_open:
            raise ValueError("Bank account not open.")
        new_balance = self.account_balance - amount
        if new_balance < 0:
            new_balance = new_balance - (amount * charge) # mal 2% additional charge
        self.account_balance = new_balance # kann auch negativ sein, daher ok
        return self.account_balance

class YouthAccount(BankAccount):
    withdraw_limit = 2000
    def __init__(self, bank_account: str, account_balance=0, monthly_interest=0.02, age=0, currency: str = "CHF"): # 2%
        super().__init__(bank_account, account_balance, currency)
        if 14 <= age <= 25:
            self.age = age
        else:
            raise ValueError("Wrong age for Youth Account.")
        self.monthly_interest = monthly_interest
        self.currency = currency
        self.withdrawn_this_month = 0

    def set_monthly_interest(self, monthly_interest):
        self.monthly_interest = monthly_interest

    def interest(self):
        interest_monthly = self.account_balance * self.monthly_interest
        return interest_monthly

    def withdraw(self, amount: float=0.0): # Geld abheben
        # withdraw_limit = 2000
        if not self.is_open:
            raise ValueError("Bank account not open.")
        if (amount + self.withdrawn_this_month) > self.withdraw_limit:
            raise ValueError("Withdraw limit exceeded.")
        new_balance = self.account_balance - amount
        if new_balance < 0: # kann nicht negativ sein
            raise ValueError("Negative balance")
        self.account_balance = new_balance # wenn ok: überschreiben
        return self.account_balance

if __name__ == "__main__":
    account = SavingsAccount("CH123456789")

    account.open_account()

    account.deposit(5000)
    print("Balance after deposit:", account.get_account_balance())

    account.withdraw(1000)
    print("Balance after withdraw:", account.get_account_balance())

    print("Начисленные проценты:", account.interest())



    account = YouthAccount(bank_account="CH987654321", account_balance=4000, age=20)

    account.open_account()

    print("Balance", account.get_account_balance())

    print("Interest accrued for the month (2%):", account.interest())

    account.withdraw(500)
    print("Balance:", account.get_account_balance())
    print("Already withdrawn this month:", account.withdrawn_this_month)

    #account.withdraw(1600)
