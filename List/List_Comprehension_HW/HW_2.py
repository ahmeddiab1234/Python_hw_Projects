# HW - 2 - Slicing and List Comprehension - Is sublist

def is_sublist(lst1, lst2):
    cnt = len(lst2)
    for idx in range(0,len(lst1)-cnt +1):
        if(lst1[idx:idx+cnt] == lst2):
            return True
    return False

print(is_sublist([1, 2, 3, 4], [1, 4]))
print(is_sublist([1, 2, 3, 4], [2, 3]))
print(is_sublist([10, -10, 20, 25, 2, 7, 2, 3], [20, 25, 2]))
print(is_sublist([10, -10, 20, 25, 2, 7, 2, 3], [20, 25, 7]))

"""
[1 2 3 4] [1 4] ⇒ False
[1 2 3 4] [2 3] ⇒ True
[10 -10 20 25 2 7 2 3] [20 25 25] ⇒ True
[10 -10 20 25 2 7 2 3] [20 25 7] ⇒ False
"""
