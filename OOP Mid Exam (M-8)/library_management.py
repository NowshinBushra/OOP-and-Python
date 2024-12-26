
# 1. Created Library Class -----------
class Library():
    _book_list = []   # 9. Protected

    @classmethod
    def entry_book(cls, book):
        cls._book_list.append(book)

    @classmethod
    def find_by_id(cls, book_id):
        for book in cls._book_list:
            if str(book._book_id) == book_id:
                return book
 

# 2. Create Book Class ------------
class Book():
    def __init__(self, book_id, title, author, availability) -> None:   # 3. Initialized Book Object
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = availability
        Library.entry_book(self)

# 4. Implemented borrow_book() method---------
    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"The book '{self._title}' borrowed successfully.")
        else:
            print(f"The book '{self._title}' is not available for borrowing.")  # 8. Error handled


# 5. Implement return_book() method -----------
    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"The book '{self._title}' returned successfully.")
        else:
            print(f"Error: The book '{self._title}' was not borrowed.") # 8. Error handled


# 6. Implement view_book_info() method ----------
    def view_book_info(self):
        if self._availability:
            status = 'Available'
        else:
            status = 'Not available'
        print(f'ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Availability: {status}')
        


def view_all_books():
    books = Library._book_list
    if books:
        print("\nLibrary Books:")
        for book in books:
            book.view_book_info()
    else:
        print("\nNo books available.")

# 7. Menu System --------------------
def menu():
    while True:
        print('\nWelcome To Library')
        print('1. View All Books')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. Exit')

        choice = input('Enter your choice: ')
    
        if choice == '1':
            view_all_books()

        elif choice == '2':
            id = input("Enter the Book ID to borrow: ")
            book = Library.find_by_id(id)
            if book:
                book.borrow_book()
            else:
                print("Error: Invalid book ID.")    # 8. Error handled

        elif choice == '3':
            id = input("Enter the Book ID to return: ")
            book = Library.find_by_id(id)
            if book:
                book.return_book()
            else:
                print("Error: Invalid book ID.")     # 8. Error handled

        elif choice == '4':
            print('Exiting the library system.')
            break
        else:
            print('Invalid choice')


book1 = Book(101, 'Physics', 'Topon', True)
book2 = Book(102, 'Math', 'Majid', False)
book3 = Book(103, 'ICT', 'Rahman', True)

menu()
