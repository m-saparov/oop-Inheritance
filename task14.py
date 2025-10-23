class User:
    def __init__(self, name):
        self.name = name

    def interact(self):
        return f"{self.name} tizim bilan o'zaro aloqada."


class Applicant(User):
    def __init__(self, name, resume):
        super().__init__(name)
        self.resume = resume

    def interact(self):
        return self.apply_to_job()

    def apply_to_job(self):
        return f"{self.name} ishga ariza topshirdi. Rezyume: {self.resume}"


class Employer(User):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def interact(self):
        return self.post_job()

    def post_job(self):
        return f"{self.name} ({self.company}) yangi ish joyini e'lon qildi."


users = [
    Applicant("Ali", "Python Developer - 3 yillik tajriba"),
    Employer("Vali", "TechnoSoft"),
]

for user in users:
    print(user.interact())
    print()
