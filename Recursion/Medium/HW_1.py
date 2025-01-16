# HW - 1 - Recursion - Medium - List Increment v2

def list_increment(lst, idx=0):
    if len(lst) == idx:
        return
    lst[idx] += len(lst) - idx
    list_increment(lst, idx+1)
    

lst = [1, 8, 2, 10, 3]
list_increment(lst)

print(lst) # 6 12 5 12 4


