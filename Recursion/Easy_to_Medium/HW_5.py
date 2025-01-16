# HW - 5 - Recursion - Easy to Medium - List average
from HW_3 import sum_lst
def list_avg(lst):
    if len(lst) ==0:
        return 0
    return sum_lst(lst) / len(lst)

print(list_avg([5]))
print(list_avg([5, 7]))
print(list_avg([1, 2, 3, 4]))