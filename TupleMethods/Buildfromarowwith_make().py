from collections import namedtuple
Book = namedtuple("Book", ["title", "author", "year"])
row = ["Ignited Minds", "Kalam", 2002]
#_make(row build from list
book = Book._make(row)
print(book.author)