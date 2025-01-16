# HW - 4 - Recursion - Easy to Medium - List max

def list_max(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    return max(lst[-1] , list_max(lst[:-1]))

print(list_max([5])) # 5
print(list_max([5, 7])) # 7
print(list_max(['most', 'saad', 'ibrahim'])) # saad

