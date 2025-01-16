from FrontEndLibrary import FrontEnd
from BackEndLibrary import BackEnd
from _Tests import test1

class LibraryManager():
    def __init__(self):
        self.book, self.user = test1()
        self.front = FrontEnd()
        # self.back = BackEnd(self.book, self.user)
        self.back = BackEnd()

    def run(self):
        while True:
            self.front.menu_option()
            choice = self.front.get_choice()
            if choice == 1:
                self._Add_Book()
            elif choice == 2:
                self._Print_Library_Books()
            elif choice == 3:
                self._Print_Books_by_Prefix()
            elif choice == 4:
                self._Add_User()
            elif choice == 5:
                self._Borrow_Book()
            elif choice == 6:
                self._Return_Book()
            elif choice == 7:
                self._Print_Users_Borrowed_Book()
            elif choice == 8:
                self._Print_Users()

    def _Add_Book(self):
        name, id, quantity = self.front.get_book_data()
        if self.back.AddBook(name, id, quantity):
            print("Book added successfully!")
        else:
            print("Failed to add book.")

    def _Print_Library_Books(self):
        books = self.back.GetBooks()
        self.front.print_library_books(books)

    def _Print_Books_by_Prefix(self):
        books = self.back.GetBooks()
        self.front.print_books_by_prefix(books)

    def _Add_User(self):
        name, id = self.front.get_user_data()
        if self.back.AddUser(name, id):
            print("User added successfully!")
        else:
            print("Failed to add user.")

    def _Borrow_Book(self):
        books = self.back.GetBooks()
        users = self.back.GetUsers()
        book_name, user_name = self.front.handle_borrow_book(books, users)
        if self.back.BorrowBook(book_name, user_name):
            print("Book borrowed successfully!")
        else:
            print("Failed to borrow the book.")

    def _Return_Book(self):
        books = self.back.GetBooks()
        users = self.back.GetUsers()
        book_name, user_name = self.front.handle_borrow_book(books, users)  
        if self.back.ReturnBook(book_name, user_name):
            print("Book returned successfully!")
        else:
            print("Failed to return the book.")

    def _Print_Users_Borrowed_Book(self):
        users = self.back.GetUsers()
        self.front.print_users_borrowed_book(users)

    def _Print_Users(self):
        users = self.back.GetUsers()
        self.front.print_users(users)


if __name__ == '__main__':
    l_manager = LibraryManager()
    l_manager.run()
