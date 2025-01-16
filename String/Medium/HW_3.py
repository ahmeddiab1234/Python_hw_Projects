# HW - 3 - Medium - String - Order Data

def order_data():
    n = int(input())
    res = []
    for _ in range(n):
        name, age, salary = input(), int(input()), int(input())
        res.append((name, age, salary))
    res.sort(key=lambda x: (len(x[0]), x[1], x[2]))
    for idx, val in enumerate(res):
        print(idx, val)

order_data()


"""
5
mostafa 33 2000
belal 10 900
mostafa 20 10000
belal 10 6000
ZIAD 2 0
"""