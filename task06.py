class Employee:
    def __init__(self, name: str, salary: float, role: str):
        self.name = name
        self.salary = salary
        self.role = role

    def calculate_bonus(self) -> tuple[int, float]:
        return 0, 0


class Developer(Employee):
    def calculate_bonus(self) -> tuple[int, float]:
        percent = 10
        bonus = self.salary * percent / 100
        return percent, bonus


class Manager(Employee):
    def calculate_bonus(self) -> tuple[int, float]:
        percent = 20
        bonus = self.salary * percent / 100
        return percent, bonus


dev = Developer("Ali", 8_000_000, "Developer")
man = Manager("Laylo", 12_000_000, "Manager")

for i in [dev, man]:
    percent, bonus = i.calculate_bonus()
    print(f"{i.name} - {i.role}: bonus - {percent}% ({bonus:,.0f} so'm)")
