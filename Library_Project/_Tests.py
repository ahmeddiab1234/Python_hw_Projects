
def test1():
    book = [
        ['math4', 100, 3, 0],
        ['math2', 101, 5, 0],
        ['math1', 102, 4, 0],
        ['math3', 103, 0, 2],
        ['prog1', 201, 3, 0],
        ['prog2', 202, 3, 0],
    ]
    user = [
        {'name': 'mostafa', 'id': 30301, 'books': [book[3]]},
        {'name': 'ali', 'id': 50501, 'books': []},
        {'name': 'noha', 'id': 70701, 'books': [book[3]]},
        {'name': 'ashraf', 'id': 90901, 'books': []}
    ]
    return book, user

# print(test1())


# print(test1())