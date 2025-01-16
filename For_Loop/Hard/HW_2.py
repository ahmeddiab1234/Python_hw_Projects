# HW - 2 - While Loop - Hard - Reverse number
N = int(input())
old_n = N
while N > 0:
    val = N % 10 
    print (val,end='')
    N = N//10
print(' ',end='')
N = old_n
while N > 0:
    val = N % 10 
    print (val*3,end='')
    N = N//10
"""
123 ⇒  321 963
"""