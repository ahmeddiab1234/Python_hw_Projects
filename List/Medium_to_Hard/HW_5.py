# HW - 2 - List - Medium to Hard - Remove evens inplace

def remove_evens_inplace(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lst.pop(i)
        else:
            i += 1
    return lst

lst = [1, 2, 3, 4, 5, 6]
print(remove_evens_inplace(lst))

lst = [-6, 6]
print(remove_evens_inplace(lst))

"""
1 2 3 4 5 6 ⇒ 1 3 5
-6 6 ⇒ Empty output
"""
