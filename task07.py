class Media:
    def __init__(self, title):
        self.title = title

    def play(self):
        return f"{self.title} ni ijro etish boshlandi."


class Song(Media):
    def play(self):
        return f"'{self.title}' qo'shig'i chalinyapti..."


class Movie(Media):
    def play(self):
        return f"'{self.title}' filmi ko'rsatilmoqda..."


class Podcast(Media):
    def play(self):
        return f"'{self.title}' podkasti eshittirilmoqda..."


media_list = [
    Song("xayr maktabim"),
    Movie("shum bola"),
    Podcast("osmondagi bolalar"),
]

for item in media_list:
    print(item.play())
