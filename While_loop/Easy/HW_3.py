# HW - While Loop - 3 - Easy - Print face down left angled triangle

num = int(input())
row = num
while row:
    
    col = row
    while col:
        print('*', end='')
        col-=1
    print()

    row-=1

