# HW - 2 - List - Medium to Hard - Is subsequence

def is_subsequence(lst1, lst2):
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            j += 1
        i += 1
    return j == len(lst2)


lst1 = [1, 2, 3, 4]
lst2 = [1, 4]
print(is_subsequence(lst1, lst2))

lst3 = [1, 2, 3, 4]
lst4 = [4, 1]
print(is_subsequence(lst3, lst4))

lst5 = [10, -10, 20, 25, 2, 7, 2, 3]
lst6 = [-10, 2, 2, 3]
print(is_subsequence(lst5, lst5))

lst7 = [10, -10, 20, 25, 2, 7, 2, 3]
lst8 = [-10, 2, 2, 2, 3]
print(is_subsequence(lst7, lst8))

"""
[1 2 3 4] [1 4] ⇒ True
[1 2 3 4] [4 1] ⇒ Fase 
[10 -10 20 25 2 7 2 3] [-10 2 2 3] ⇒ True
[10 -10 20 25 2 7 2 3] [-10 2 2 2 3] ⇒ False
"""

