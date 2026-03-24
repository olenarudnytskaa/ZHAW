class BankAccount:
    def __init__(self, bank_account: str, account_balance: float=0.0, currency: str="CHF"):
        self.is_open = False # Bankkonto per default geschlossen
        self.bank_account = bank_account # IBAN
        self.account_balance = account_balance # Guthaben
        self.currency = currency # Währung

    def open_account(self): # Bankkonto öffnen
        self.is_open = True

    def close_account(self): # Bankkonto schliessen
        self.is_open = False

    def deposit(self, amount: float=0.0): # Geld einzahlen
        if not self.is_open:
            raise ValueError("Bank account not open.")
        new_balance = self.account_balance + amount
        if new_balance > 100000.0: # kann nicht über CHF 100'000 sein
            raise ValueError("Balance too high")
        self.account_balance = new_balance # wenn ok: überschreiben
        return self.account_balance

    def withdraw(self, amount: float=0.0): # Geld abheben
        if not self.is_open:
            raise ValueError("Bank account not open.")
        new_balance = self.account_balance - amount
        if new_balance < 0: # kann nicht negativ sein
            raise ValueError("Negative balance")
        self.account_balance = new_balance # wenn ok: überschreiben
        return self.account_balance

    def get_account_balance(self): # Kontostand abfragen
        return self.account_balance


if __name__ == "__main__":
    account = BankAccount("CH123456789")

    account.open_account()
    account.deposit(5000)
    print("Balance after deposit:", account.get_account_balance())

    account.withdraw(1000)
    print("Balance after withdraw:", account.get_account_balance())

    account.close_account()