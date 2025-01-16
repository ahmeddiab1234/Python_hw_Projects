# HW - 1 - Hard - Variables - Swapping 3 numbers!

num1, num2, num3 = map(int, input().split()) # 115 20 30

swap_var1 = num1 # swap1 = 115
num1 = num2 # num1 = 20
num2 = num3 # num3 = 30
num3 = swap_var1 # num3 = 115

print(num1, num2, num3)