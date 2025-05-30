class Library:
    def __init__(self, books):
        self.__books = books
    def __check_availability(self, book):
        return book in self.__books
    def search_book(self, book):
        return self.__check_availability(book)
    def return_book(self, return_book):
        self.__books.append(return_book)
    


library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
print(library._Library__books)
print(library.search_book("Moby-Dick"))
print(library.search_book("Jane Air"))