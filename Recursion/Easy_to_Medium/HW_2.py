# HW - 2- Recursion - Easy to Medium - Power function
def my_pow(value, p = 2):
    if p==0:
        return 1
    return value * my_pow(value, p-1)

print(my_pow(7)) # 49
print(my_pow(7, 0)) # 1
print(my_pow(7, 3)) # 343

