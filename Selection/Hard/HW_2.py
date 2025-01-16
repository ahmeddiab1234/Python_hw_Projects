# HW - 2 - Hard - Selection - Two Intervals Intersection

a, b, c, d = map(int, input().split())

i1, i2 = -1, -1
if c >= a and d >= b and b > c:
    i1, i2 = c, b
elif a >= c and b >=d and d > a:
    i1, i2 = a, d
elif a <= c and b <= d and c == b:
    i1, i2 = b, c
elif a >= c and b >= d and a == d:
    i1, i2 = a, d
elif a >= c and d >= b:
    i1, i2 = a, b
elif c >= a and b >= d:
    i1, i2 = c, d
elif a == c and b == d:
    i1, i2 = a, b
elif a > c and b > d and b > c:
    pass

if i1 != -1 and i2 != -1:
    print(i1, i2)
else:
    print(-1)

"""
1. 1 6 3 8 ⇒ 3 6
2. 1 15 20 30 ⇒ -1 
3. 10 20 15 25 ⇒ 15 20
4. 5 10 0 15 ⇒ 5 10 
5. 0 5 5 10 ⇒ 5 5 
6. 3 8 3 8 ⇒ 3 8 
7. 1 3 5 7 ⇒ -1 
8. 10 10 5 15 ⇒ 10 10

"""