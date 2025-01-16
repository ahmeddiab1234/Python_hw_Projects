# hW - 3 - Medium - While Loop - Special multiples 2

num = int(input())

start = 2
while num > 0:
    if start % 3 == 0 and start % 4 !=0:
        print(start, end=' ')
        num -=1
    start +=1

"""
11
3 6 9 15 18 21 27 30 33 39 42
"""
