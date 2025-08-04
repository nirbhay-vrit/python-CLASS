class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author

    def get_info(self):
        print(f"'{self.title}' is written by {self.author.name}")

a = Author("J.K. Rowling")
b = Book("Harry Potter", a)

b.get_info()
