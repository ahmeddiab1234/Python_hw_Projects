# HW - 3 - Hard - While Loop - Multiplication table

N,M = map(int,input().split())
start_n = 1
while start_n <= N:
    start_m = 1
    while start_m <= M:
        print(f'{start_n} X {start_m} = {start_n*start_m}')
        start_m +=1
    start_n +=1

"""
3 4
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
"""