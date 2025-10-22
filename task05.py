
class Appliance:
    def turn_on(self):
        return "appliance yoqildi"

    def turn_off(self):
        return "appliance o'chirildi"


class TV(Appliance):
    def turn_on(self):
        return "TV yoqildi"

    def turn_off(self):
        return "TV o'chirildi"


class Fridge(Appliance):
    def turn_on(self):
        return "Muzlatkich yoqildi"

    def turn_off(self):
        return "Muzlatkich o'chirildi"

apps = [
    TV(),
    Fridge(),
    Appliance()
]

for app in apps:
    print(app.turn_on())
    print(app.turn_off())
    print()