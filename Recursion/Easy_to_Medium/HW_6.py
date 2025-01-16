# HW - 6 - Recursion - Easy to Medium - List Increment v1

def list_increment(lst):
    if len(lst) ==0:
        return []
    inc = len(lst)
    return [inc +lst[0] ] + list_increment(lst[1:])

print(list_increment([1, 8, 2, 10, 3])) # 6 12 5 12 4