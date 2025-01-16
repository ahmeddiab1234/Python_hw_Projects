# HW - 3 - Medium - Function - Get nth-prime

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

for i in range(1, 10):
    print(i, nth_prime(i))


"""
output:
1 2 
2 3
3 5
4 7
5 11
6 13
7 17
8 19
9 23
"""