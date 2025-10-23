class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_delivery_method(self):
        return "Yetkazib berish usuli aniqlanmagan."

    def download(self):
        return "Bu mahsulotni yuklab bo'lmaydi."


class PhysicalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name} mahsuloti kuryer orqali 3 kunda yetkaziladi."

    def download(self):
        return "Jismoniy mahsulot yuklab olinmaydi."


class DigitalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name} raqamli mahsulot, onlayn tarzda taqdim etiladi."

    def download(self):
        return f"{self.name} faylini yuklab olish boshlandi..."


products = [
    PhysicalProduct("Kitob", 120000),
    DigitalProduct("Python kursi", 250000),
]

for product in products:
    print(f"Mahsulot: {product.name} - {product.price} so'm")
    print(product.get_delivery_method())
    print(product.download())
    print()
