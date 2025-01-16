# HW - 1 - Hard - Selection - Intervals

X = int(input())
s1, e1, s2, e2, s3, e3 = map(int,input().split())

num = 0
if X >= s1 and X <= e1:
    num +=1

if X >= s2 and X <= e2:
    num +=1

if X >= s3 and X <= e3:
    num +=1

print(num)

"""
7 1 10 5 6 4 40 ⇒ 2
10 5 15 6 100 3 30 ⇒ 3
10 100 200 100 101 120 170 ⇒ 0
"""