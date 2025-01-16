# hW - 4 - Medium - While Loop - Minimum of values

T = int(input())
while T > 0:
    n = int(input())
    min = float('inf')
    while n > 0:
        val = int(input())
        if val < min:
            min = val
        n -=1
    print(f'Min Value is : {min}')
    T -=1
