class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            return f"{amount}$ yechildi. Yangi balans: {self.balance}$"
        else:
            return "Yetarli mablag' yo'q."

    def get_interest(self):
        return 0


class SavingsAccount(BankAccount):
    def get_interest(self):
        interest = self.balance * 0.05
        return f"Foiz: {interest}$ (5%)"

    def withdraw(self, amount):
        if amount < 0:
            return "amout manfiy bo'la olmaydi!"
        elif amount > self.balance:
            return "amout balancedan katta!"
        return super().withdraw(amount)


class CheckingAccount(BankAccount):
    def get_interest(self):
        return f"Bu hisob turi foiz bermaydi."

    def withdraw(self, amount):
        if self.balance < amount:
            return "limitidan o'tib bo'lmaydi!"
        self.balance -= amount
        return f"{amount}$ yechildi (CheckingAccount). Yangi balans: {self.balance}$"


accounts = [
    SavingsAccount("Ali", 1000),
    CheckingAccount("Vali", 200),
]

for acc in accounts:
    print(f"\n{acc.owner} hisobi:")
    print(acc.withdraw(600))
    print(acc.get_interest())
