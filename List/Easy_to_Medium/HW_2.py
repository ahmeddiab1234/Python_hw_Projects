# HW - 2 - List - Easy to Medium - Replace MinMax

def replace_min_max_inplace(lst):
    min_val = min(lst)
    max_val = max(lst)
    for i in range(len(lst)):
        if lst[i] == min_val:
            lst[i] = max_val
        elif lst[i] == max_val:
            lst[i] = min_val

lst1 = [4, 1, 3, 10, 8, 10, 10]
replace_min_max_inplace(lst1)
print(lst1)


"""
4 1 3 10 8 10 10 ⇒ 4 10 3 1 8 1 1
""" 