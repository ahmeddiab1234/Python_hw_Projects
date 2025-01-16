# HW - For Loop - 6 - Medium To Hard - Digits sum in range

n,a,b = map(int, input().split())
res =0

for i in range (1,n+1):
    val = sum(int(x) for x in str(i)) 
    if a <= val <= b:
        res += i

print(res)

