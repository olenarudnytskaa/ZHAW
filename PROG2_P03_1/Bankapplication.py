import Subaccounts
from currency import currency_exchange

class TaxReport: # Tax Report Generator -> Steuerausweis
    def generate(self, bank_app):
        total_savings = 0
        total_youth = 0
        #sum wealth for submission for tax => Vermögen aufsummieren für Steuern
        for account in bank_app.accounts:
            balance = account.get_account_balance()

            # Umrechnung falls nicht CHF
            if account.currency != "CHF":
                rate = currency_exchange(account.currency)
                converted = balance * rate
                print(f"Converting {balance} {account.currency} → {converted:.2f} CHF")
            else:
                converted = balance

            if isinstance(account, Subaccounts.SavingsAccount):
                total_savings += converted
            elif isinstance(account, Subaccounts.YouthAccount):
                total_youth += converted
        return f"Tax report 2021 for fiscal year 2020\n** Savings Account ** {total_savings:.2f} Fr\n** Youth Account ** {total_youth:.2f} Fr"


class BankApplication:
    def __init__(self):
        self.accounts = []
        self.current_account = None

        # Ergänzt: einfache Login-Funktion vor dem Menü.

    def authenticate(self):
        print("Login erforderlich")
        username = input("Benutzername: ").strip() #admin
        password = input("Passwort: ").strip() #1234

        if username == "admin" and password == "1234":
            self.authenticated = True
            return "Authentifizierung erfolgreich."

        return "Authentifizierung fehlgeschlagen."

    def open_account(self): # Konto öffnen

         # Konto erstellen und in self.accounts speichern.
        while True:
            acc = input("Was für ein Konto möchtest du eröffnen?\n1 CH123 SavingsAccount\n2 CH456 YouthAccount\n")
            if acc == "1":
                # Für Einfachheit wird immer Konto CH123 geöffnet
                account = Subaccounts.SavingsAccount("CH123", 1000, "CHF")
                account.open_account()
                self.accounts.append(account)
                self.current_account = account  # Ergänzt: neu eröffnetes Konto sofort auswählen
                return "SavingsAccount erstellt"
            elif acc == "2":
                # Für Einfachheit wird immer Konto CH456 geöffnet
                account = Subaccounts.YouthAccount("CH456", 1000, age=18, currency="CHF")
                account.open_account()
                self.accounts.append(account)
                self.current_account = account  # Ergänzt: neu eröffnetes Konto sofort auswählen
                return "YouthAccount erstellt"
            else:
                print("Ungültige Eingabe")

    def select_account(self): # Konto auswählen
        if not self.accounts:
            return "Keine Konten vorhanden."

        while True:
            print("Konten:")
            for i, acc in enumerate(self.accounts):
                print(i + 1, acc.bank_account)

            choice = int(input("Nummer wählen: "))
            if 1 <= choice <= len(self.accounts):
                self.current_account = self.accounts[choice - 1]
                return self.current_account.bank_account + " ausgewählt"
            else:
                print("Ungültige Auswahl")


    def deposit(self): # Geld einzahlen
        if self.current_account is None:
            return "Kein Konto ausgewählt."
        amount = float(input("Wie viel Geld möchtest du einzahlen? "))
        try:
            new_balance = self.current_account.deposit(amount)
            return f"Neuer Kontostand: {new_balance}"
        except ValueError as error:
            return str(error)

    def withdraw(self): # Geld abheben
        if self.current_account is None:
            return "Kein Konto ausgewählt."
        amount = float(input("Wie viel Geld möchtest du abheben? "))
        try:
            new_balance = self.current_account.withdraw(amount)
            return f"Neuer Kontostand: {new_balance}"
        except ValueError as error:
            return str(error)

    def show_balance(self): # Kontostand abfragen
        if self.current_account is None:
            return "Kein Konto ausgewählt."
        balance = self.current_account.get_account_balance()
        return f"Kontostand: {balance} {self.current_account.currency}"

    def add_mandate(self):  # Ergänzt: Zugriff erlauben
        if self.current_account is None:
            return "Kein Konto ausgewählt."

        name = input("Name des Mandatars: ")

        # wenn Liste noch nicht existiert -> erstellen
        if not hasattr(self.current_account, "mandates"):
            self.current_account.mandates = []

        self.current_account.mandates.append(name)

        return f"{name} hat jetzt Zugriff."

    def close_account(self): # Konto schliessen
        if self.current_account is None:
            return "Kein Konto ausgewählt."
        self.current_account.close_account()
        return "Konto wurde geschlossen."


    def menu(self): #hier wird ausgewählt
        while True:
            choice = input("Was möchtest du tun\n1 Konto öffnen\n2 Konto auswählen\n3 Geld einzahlen\n4 Geld abheben\n5 Kontostand abfragen\n6 Konto schliessen\n7 Zugriffsberechntigung\n8 Tax report\n0 Exit\n")
            if choice == "1": # Konto öffnen
                print(self.open_account())
            elif choice == "2": # Konto auswählen
                print(self.select_account())
            elif choice == "3": # Geld einzahlen
                print(self.deposit())
            elif choice == "4": # Geld abheben
                print(self.withdraw())
            elif choice == "5": # Kontostand abfragen
                print(self.show_balance())
            elif choice == "6": # Konto schliessen
                print(self.close_account())
            elif choice == "8": # Steuerausweis
                report = TaxReport()
                print(report.generate(self))
            elif choice == "7": # Zugriff Erlaubnis
                print(self.add_mandate())
            elif choice == "0": # exit
                print("Programm beendet.")
                break
            else:
                print("Invalid input")

if __name__ == "__main__":
    app = BankApplication()
    app.authenticate()
    app.menu()