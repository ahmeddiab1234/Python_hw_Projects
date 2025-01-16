# HW - 2- Recursion - Easy to Medium - List sum

def sum_lst(lst):
    if len(lst) ==0:
        return 0
    return lst[-1] + sum_lst(lst[:len(lst)-1])
"""
print(sum_lst([])) # 0
print(sum_lst([5])) # 5
print(sum_lst([5, 7])) # 12

"""
