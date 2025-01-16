# HW - 3 - Selection - If condition - Easy - Maximum but constrained

num1,num2,num3 = map(int,input().split())

if(num1<100 or num2<100 or num3<100):
    if(num1<100 and num2<100 and num3<100):
        if num1>=num2 and num1>=num3:
            print(num1)
        elif num2>=num1 and num2>=num3:
            print(num2)
        else:
            print(num3)

    elif num1<100 and num2<100:
        if(num1>=num2):
            print(num1)
        else:
            print(num2)

    elif num1<100 and num3<100:
        if(num1>=num3):
            print(num1)
        else:
            print(num3)
    elif num2<100 and num3<100:
        if(num2>=num3):
            print(num2)
        else:
            print(num3)
    elif num1<100:
        print(num1)
    elif num2<100:
        print(num2)
    elif num3<100:
        print(num3)
else:
    print(-1)


"""
22 90 115 ⇒ 90
200 300 400 ⇒ -1
50 100 150 ⇒ 50
10 30 20 ⇒ 30
"""