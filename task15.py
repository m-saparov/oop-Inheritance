class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return f"{self.name} hujumga tayyorlanmoqda..."

    def defend(self):
        return f"{self.name} himoyalanmoqda..."


class Warrior(Character):
    def attack(self):
        return f"{self.name} qilich bilan kuchli zarba berdi!"

    def defend(self):
        return f"{self.name} qalqon yordamida zarbani to'sdi."


class Mage(Character):
    def attack(self):
        return f"{self.name} yong'in sehrini ishlatdi!"

    def defend(self):
        return f"{self.name} sehrli qalqon hosil qildi."


class Archer(Character):
    def attack(self):
        return f"{self.name} kamondan o'q uzdi!"

    def defend(self):
        return f"{self.name} tezlik bilan hujumdan chetlandi."


characters = [
    Warrior("Arslan", 120),
    Mage("Malika", 100),
    Archer("Rustam", 90),
]

for ch in characters:
    print(f"{ch.name}:")
    print(ch.attack())
    print(ch.defend())
    print()
