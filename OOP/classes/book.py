class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

setattr(Book, 'rating', 8.7)
setattr(Book, 'genre', 'dystopian')

del Book.pages
delattr(Book, 'writer')
delattr(Book, 'rating')

print(Book.__dict__)