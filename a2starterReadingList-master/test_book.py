"""
(incomplete) Tests for Book class
"""
from book import Book

# test empty book (defaults)
book = Book()
print(book)
assert book.author == ""
assert book.title == ""
assert book.pages == 0

# test initial-value book
book2 = Book("Fish fingers", "Dory", 2, 'r')
print(book2)

book3 = Book("Fish ", "mark", 2, 'r')
print(book3)
# test mark_completed()
