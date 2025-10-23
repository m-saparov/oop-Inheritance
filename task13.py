class Courier:
    def __init__(self, name):
        self.name = name

    def delivery_range(self):
        return "Yetkazib berish masofasi aniqlanmagan."

    def calculate_fee(self, distance):
        return 0


class BikeCourier(Courier):
    def delivery_range(self):
        return "Velokurier 5 km gacha xizmat ko'rsatadi."

    def calculate_fee(self, distance):
        base = 5000
        if distance <= 5:
            return base + distance * 1000
        return "Masofa juda uzoq, velokurier yetkaza olmaydi."


class CarCourier(Courier):
    def delivery_range(self):
        return "Avtokurier 30 km gacha xizmat ko'rsatadi."

    def calculate_fee(self, distance):
        base = 10000
        if distance <= 30:
            return base + distance * 2000
        return "Masofa juda uzoq, avtokurier yetkaza olmaydi."


class DroneCourier(Courier):
    def delivery_range(self):
        return "Dron 10 km radiusda tez yetkazib beradi."

    def calculate_fee(self, distance):
        base = 15000
        if distance <= 10:
            return base + distance * 500
        return "Masofa juda uzoq, dron ucholmaydi."


couriers = [
    BikeCourier("Bike-1"),
    CarCourier("Car-1"),
    DroneCourier("Drone-1"),
]

for c in couriers:
    print(f"Kuryer: {c.name}")
    print(c.delivery_range())
    print("10 km uchun xizmat narxi:", c.calculate_fee(10))
    print()
