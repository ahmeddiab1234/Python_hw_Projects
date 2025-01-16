# HW - Selection  - If condition - Easy - 2 - Sort 3 numbers

num1, num2, num3 = map(int, input().split())
max1, max2, max3 = num1, num2, num3

if num1 >= num2 and num1 >= num3:
    max1 = num1
    if num2 >= num3:
        max2 = num2
        max3 = num3
    else:
        max2 = num3
        max3 = num2
elif num2 >= num3 and num2 >= num1:
    max1 = num2
    if num1 >= num3:
        max2 = num1
        max3 = num3
    else:
        max2 = num3
        max3 = num1
else:
    max1 = num3
    if num2 >= num1:
        max2 = num2
        max3 = num1
    else:
        max2 = num1
        max3 = num2

print(max3, max2, max1)


"""
○ 1 2 3 ⇒ 1 2 3
○ 1 3 2 ⇒ 1 2 3
○ 2 1 3 ⇒ 1 2 3
○ 2 3 1 ⇒ 1 2 3
○ 3 1 2 ⇒ 1 2 3
○ 3 2 1 ⇒ 1 2 3
"""