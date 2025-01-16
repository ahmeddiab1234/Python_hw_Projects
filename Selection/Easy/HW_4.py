# HW - 4 - Selection - If condition - Easy - Conditional Count

x = int(input())
num1,num2,num3,num4,num5 = map(int,input().split())

greater_x,smaller_x = 0,0
if num1>x:
    greater_x+=1
else :
    smaller_x+=1

if num2>x:
    greater_x+=1
else :
    smaller_x+=1

if num3>x:
    greater_x+=1
else :
    smaller_x+=1

if num4>x:
    greater_x+=1
else :
    smaller_x+=1

if num5>x:
    greater_x+=1
else :
    smaller_x+=1

print(smaller_x, greater_x)

# 10 300 1 5 100 200
# greater + smaller = x