# HW - For Loop - 4 - Medium To Hard - Is Prime

n = int(input())

if n<=1 :
    print("NO")
elif n==2:
    print("YES")

elif n%2==0:
    print("NO")

else:
    for i in range(2,n):
        if n%i==0:
            print("NO")
            break
    else:
        print("YES")

