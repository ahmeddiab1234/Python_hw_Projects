# HW - Selection - If condition - Easy - 1 Arithmetic

num1,num2 = map(int, input().split())

is_odd1 = num1%2==1
is_odd2 = num2%2==1
if is_odd1 and is_odd2:
    print(num1*num2)
elif not is_odd1 and not is_odd2:
    if(num2>0):
        print(num1/num2)
    else:
        print("Error, Number 2 is 0")
elif is_odd1 and not is_odd2:
    print(num1+num2)
elif not is_odd1 and is_odd2:
    print(num1-num2)


"""
○ 5 7 => 35
○ 12 2 => 6
○ 5 6 => 11
○ 12 3 => 9
"""