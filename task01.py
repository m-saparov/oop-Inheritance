class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"{self.name} is speaking!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} is barking (woof)"

class Cat(Animal):
    def speak(self):
        return f"{self.name} is meowing!"


animals = [
    Dog("Bobik"),
    Cat("Mushuk"),
    Animal("Hayvon")
]


for animal in animals:
    print(animal.speak())
