
class User:
    def __init__(self, name):
        self.name = name

    def access_level(self):
        return f"{self.name} - kirish huquqiga egami?"

class Admin(User):
    def access_level(self):
        return f"{self.name} - kirish huquqiga ega"
    
class Guest(User):
    def access_level(self):
        return f"{self.name} - kirish huquqiga ega emas!"
    

u1 = User("Ali")
a1 = Admin("Vali")
g1 = Guest("Soli")

print(u1.access_level())
print(a1.access_level())
print(g1.access_level())
