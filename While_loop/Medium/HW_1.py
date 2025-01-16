# HW - 1 - Medium - While Loop - Print Diamond

N = int(input())

row = 1

while row <= N:

    spaces = 1
    while spaces <= N-row:
        print(' ', end='')
        spaces +=1
    
    starts = 1
    while starts <= 2*row -1:
        print('*',end='')
        starts +=1
    print()
    row +=1
    
row = N

while row > 0:

    spaces = 1
    while spaces <= N-row:
        print(' ', end='')
        spaces +=1
    
    starts = 1
    while starts <= 2*row -1:
        print('*',end='')
        starts +=1
    print()
    row -=1
    

