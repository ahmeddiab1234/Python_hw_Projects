# hW - 2 - Medium - While Loop - Special multiples 1

num = int(input())
start = 0
while start <= num:
    if (start % 8 == 0) or (start % 3 == 0 and start % 4 == 0):
        print(start, end = ' ')
    start +=1

"""
100
0 8 12 16 24 32 36 40 48 56 60 64 72 80 84 88 96
"""