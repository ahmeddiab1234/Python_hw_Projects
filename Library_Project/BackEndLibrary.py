class BackEnd():
    def __init__(self, book_data=None, user_data=None):
        self.Books = book_data if book_data else []
        self.Users = user_data if user_data else []

    def AddBook(self, name, id, quantity):
        if name and id and quantity:
            self.Books.append([name, id, quantity, 0])
            return True
        return False

    def AddUser(self, name, id):
        if name and id:
            self.Users.append({'name': name, 'id': id, 'books': []})
            return True
        return False

    def BorrowBook(self, book_name, user_name):
        if self.Books and self.Users:
            for idx, (name, id, quantity, borrowed) in enumerate(self.Books):
                if book_name == name and quantity > 0:
                    self.Books[idx][2] -= 1 
                    self.Books[idx][3] += 1 
                    for u in self.Users:
                        if u['name'] == user_name:
                            u['books'].append(self.Books[idx])
                            return True
                elif book_name == name and quantity <= 0:
                    return False
        return False

    def ReturnBook(self, book_name, user_name):
        if self.Books and self.Users:
            for idx, (name, id, quantity, borrowed) in enumerate(self.Books):
                if book_name == name and borrowed > 0:
                    self.Books[idx][2] += 1 
                    self.Books[idx][3] -= 1
                    for u in self.Users:
                        if u['name'] == user_name:
                            u['books'].remove(self.Books[idx])
                            return True                        
                elif book_name == name and borrowed <= 0:
                    return False
        return False

    def GetBooks(self):
        return self.Books
    
    def GetUsers(self):
        return self.Users
