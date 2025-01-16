
class FrontEnd():
    def __init__(self):
        pass
    def menu_option(self):
        options = [
            '1) Add book',
            '2) Print library books',
            '3) Print books by prefix',
            '4) Add user',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print users'
        ]
        print('\n'.join(options))


    def get_choice(self):
        while True:
            try:
                choice = int(input('Enter your choice (from 1 to 8): '))
                if 1 <= choice <= 8:
                    return choice
                print("Invalid range. Please enter a number between 1 and 8.")
            except ValueError:
                print('Invalid input, Please Enter an integer.')


    def get_book_data(self):
        print('Enter book info: ')
        book_name = input('Enter name: ')
        while True:
            try:
                book_id = int(input('Enter id: '))
                total_quantity = int(input('Total quantity: ')) 
                if book_id < 0:
                    raise ValueError('The id must be positive. ')
                if total_quantity >=0:
                    return book_name, book_id, total_quantity
                print('Error: the quantity number must be positive. ')
            except ValueError:
                print('Invalid input, Please Enter an integer.')


    def get_user_data(self):
        print('Enter user info: ')
        user_name = input('Enter user name: ')
        try:
            user_id = int(input('Enter id: '))
            if user_id >= 0:
                return user_name, user_id
            print('Error: the id must be positive. ')
        except ValueError:
            print('Invalid input, Please Enter an integer.')


    def print_library_books(self, book):
        if book:
            for name, id, quantity, borrowed in book:
                print(f'Book name: {name}    -    id: {id}  -   total quantity: {quantity}   -   total borrowed {borrowed}')
            return True
        
        print('There is no books yet in the library. ') 


    def print_books_by_prefix(self, book):
        pref = input('Enter book name prefix: ')
        if book:
            for name, id, quantity, borrowed in book:
                if pref in name:
                    print(f'Book name: {name}    -    id: {id}  -   total quantity: {quantity}   -   total borrowed {borrowed}')
            return True
        
        print('There is books contain this prefix. ') 


    def print_users_borrowed_book(self, user):
        if user:
            book_name = input('Enter name: ')
            print('List of users borrowed this book ')
            for values in user:
                u_name, u_id, boorrowed = values['name'], values['id'], values['books']
                if boorrowed:
                    for b_name, _, _, _ in boorrowed:
                        
                        if b_name == book_name:
                            print(f'User name: {u_name} \t - id: {u_id} ')
            print()
            return True

        print('There are no users borrow books yet ')


    def print_users(self, user):
        if user:
            for values in user:
                name, id, boorrowed = values['name'], values['id'], values['books']
                print(f'User name: {name} \t - id: {id} ')
                if boorrowed:
                    print('---> Borrowed books:')
                    for b_name, b_id, tot_quantity, tot_borrowed in boorrowed:
                        print(f'--->Book name: {b_name} \t - if: {b_id} - total quantity: {tot_quantity} - total borrowed: {tot_borrowed} ')
                print()
            return True

        print('There are no users loged in the library ')


    def handle_borrow_book(self, book, user):
        while True:
            print('Enter user name and book name ')
            try:
                u_name = input('User name: ')
                is_valid_user_name = [u for u in user if u['name'] == u_name]
                if not is_valid_user_name:
                    print('Error: Invalid user name! Please try again.')
                    continue
                    
                b_name = input('Book name: ')
                for idx, (name, id, quantity, borrowed) in enumerate(book):
                    if b_name == name and quantity > 0:
                        return b_name, u_name
                    elif b_name == name and quantity <= 0:
                        print('Error: Failed to borrow the book. No available quantity.')
                        return None
                
                print('Error: The book is not found in the library.')
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


    def handle_return_book(self, book, user):
        while True:
            print('Enter user name and book name ')
            try:
                u_name = input('User name: ')
                is_valid_user_name = [u for u in user if u['name'] == u_name]
                if not is_valid_user_name:
                    print('Error: Invalid user name! Please try again.')
                    continue
                    
                b_name = input('Book name: ')
                for idx, (name, id, quantity, borrowed) in enumerate(book):
                    if b_name == name and borrowed > 0:
                        return b_name, u_name
                    elif b_name == name and borrowed <= 0:
                        print('This user did not borrow this book.')
                        return None
                
                print('Error: The book is not found in the library.')
            except Exception as e:
                print(f"An unexpected error occurred: {e}")



if __name__ == '__main__':
    front = FrontEnd()
    from _Tests import test1
    books, users = test1()

    # front.menu_option()
    # front.get_choice()
    # front.get_book_data()
    # front.get_user_data()
    # front.print_library_books(books)
    # front.print_users(users)
    # front.print_users_borrowed_book(users)
    # front.print_books_by_prefix(books)
    print(front.handle_borrow_book(books, users))


