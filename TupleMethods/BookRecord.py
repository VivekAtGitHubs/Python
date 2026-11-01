from collections import namedtuple
Book = namedtuple("Book", ["title", "author", "year"])
book = Book("Wings of Fire", "Kalam", 1999)
print(book.author)
print(book.year)