class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        print(f"{self.title} - {self.author.name}")

author1 = Author("Dickens", "Englishman")
book = Book("война и мир", author1)
book.get_info()
print(author1.name)
print(author1.nationality)

