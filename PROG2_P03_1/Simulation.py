import Subaccounts
import time
import random
import datetime

# alle 10s = 1 Monat, dann zins berechnen und Balance überschreiben & Limite neu setzen

class Bank:
    def __init__(self, accounts_list):
        self.accounts = accounts_list #YouthAccount,SavingsAccount
        self.current_date = datetime.date.today()#Startdatum auf heute setzen

    def make_random_expense(self, account):
        expense_type = random.choice(["small", "medium", "large"])

        if expense_type == "small":
            amount = random.randint(5, 50)  # Kleine Ausgaben-kafe oder Ticket
            print(f"  -> Petty expense: {amount}")
        elif expense_type == "medium":
            amount = random.randint(51, 300)  # Mittlere Ausgaben, Einkaufen
            print(f"  -> Average expense: {amount}")
        else:
            amount = random.randint(301, 1500)  # Große Ausgaben, Miete bezahlen
            print(f"  -> A big expense: {amount}")


        try:
            account.withdraw(amount)
            print(f"  New balance: {account.get_account_balance():.2f}")
        except ValueError as error:
            print(f"  Abgelehnt: {error}")

    def simulate_month(self):
        print("\n" + "=" * 40)
        print("⏳ Monat endet... Berechnung läuft")

        # 10 Sekunden Pause
        time.sleep(10)

        # Datum um 30 Tage verschieben
        self.current_date = self.current_date + datetime.timedelta(days=30)
        print(f"Current date: {self.current_date}")
        print("=" * 40)

        # 3. Schleife durch alle Konten
        for account in self.accounts:

            # Zinsen berechnen und einzahlen
            interest_amount = account.interest()
            if interest_amount > 0:
                try:
                    account.deposit(interest_amount)
                    print(f"Interest accrued: {interest_amount:.2f}")
                except ValueError as error:
                    print(f"Interest could not be added: {error}")

            # Zähler zurücksetzen
            # Jugendkonto
            if isinstance(account, Subaccounts.YouthAccount):
                account.withdrawn_this_month = 0
                print(f"The withdrawal limit has been reset for youth accounts!")


if __name__ == "__main__":
    # Kontos erstellen mit limit 4000chf
    my_savings = Subaccounts.SavingsAccount(bank_account="CH-SAV-111", account_balance=4000)
    my_youth = Subaccounts.YouthAccount(bank_account="CH-YOU-222", account_balance=4000, age=20)

    # open
    my_savings.open_account()
    my_youth.open_account()

    #
    my_bank = Bank([my_savings, my_youth])

    #start
    print(f"Starting balance on both accounts: 4000")

    # Simulation für 3 Monate
    for month in range(1, 4):
        print(f"\n Month runs №{month}")

        # 3 einkaufen
        for i in range(3):
            print(f"\n shopping {i + 1} for YouthAccount:")
            my_bank.make_random_expense(my_youth)

            # pause
            time.sleep(1)

            # End des Monats Pause 10 sekunden, % und Limiten
        my_bank.simulate_month()

    #end des Simulation
    print(f"Savings Conto: {my_savings.get_account_balance():.2f}")
    print(f"Youth Conto: {my_youth.get_account_balance():.2f}")