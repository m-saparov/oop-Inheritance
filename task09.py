class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        return f"{self.recipient} ga xabar yuborilmoqda..."


class EmailNotification(Notification):
    def send(self):
        return f"Email {self.recipient} manziliga yuborildi:\n{self.message}"


class SMSNotification(Notification):
    def send(self):
        return f"SMS {self.recipient} raqamiga yuborildi:\n{self.message}"


notifications = [
    EmailNotification("user@example.com", "Salom"),
    SMSNotification("+998901234567", "test uchun message."),
]

for note in notifications:
    print(note.send())
    print()
