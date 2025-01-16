# HW - Operator - 1 - Medium - Is even?

num = int(input())

is_even1 = num % 2 == 0
is_even2 = num % 10 == 0 or num % 10 % 2 == 0
is_even3 = num / 2 == int(num / 2)

print(is_even1, is_even2, is_even3)
