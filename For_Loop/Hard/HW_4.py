# HW - 4 - While Loop - Hard - Special Sum

T = int(input())
while T >0:
    N = int(input())
    range_n = 0
    res = 0
    while range_n < N:
        n_copy = range_n
        sum =1
        val = int(input())
        while n_copy >=0:
            sum *= val
            n_copy -=1
        range_n +=1
        res += sum
    print(f'Sum is {res}')

    T -=1
