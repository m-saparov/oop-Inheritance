class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_preview(self):
        return f"'{self.title}' hujjati uchun oldindan ko'rish tayyorlanmoqda..."


class WordDocument(Document):
    def print_preview(self):
        return f"Word hujjati: {self.title}.docx\nMatn namunasi: {self.content[:40]}..."


class PdfDocument(Document):
    def print_preview(self):
        return f"PDF fayl: {self.title}.pdf\nSahifa ko'rinishi (1-bet): {self.content[:40]}..."


documents = [
    WordDocument("Hisobot", "Bu yilgi moliyaviy natijalar haqida batafsil hisobot..."),
    PdfDocument("Shartnoma", "Tomonlar quyidagi shartlar asosida kelishib oldilar..."),
]

for doc in documents:
    print(doc.print_preview())
    print()
