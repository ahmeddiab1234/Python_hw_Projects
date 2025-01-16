# HW - For Loop - 5 - Medium To Hard - Print Primes

n = int(input())

for i in range(2, n+1):
    if i == 2:
        print(i, end=' ')
    if i % 2 == 0:
        continue
    is_prime = True
    for x in range(2, i):
        if i % x == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')

# input -> 18 . output -> 2 3 5 7 11 13 17


