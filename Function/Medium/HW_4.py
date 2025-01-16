# HW - 4 - Medium - Function - Get nth-fibonacci

def nth_fib(n):
    if n==1 or n==2:
        return n-1
    num1,num2 =0,1
    n-=2
    while n > 0:
        res = num1+num2
        num1 = num2
        num2= res
        n -= 1
    return res
    

for i in range(1,10):
    print(i, nth_fib(i))

"""

1 0
2 1
3 1
4 2
5 3
6 5
7 8
8 13
9 21

"""