# HW - 4 - List - Easy to Medium - Unique Numbers of unordered

def unique_list(lst):
    res = []
    freq = [False] * len(lst)
    for num in lst:
        if not freq[num]:
            res.append(num)
            freq[num] = True
    return res

lst1 = [1, 5, 5, 2, 5, 7, 2, 3, 3, 3, 5, 2, 7]
print(unique_list(lst1))


"""
1 5 5 2 5 7 2 3 3 3 5 2 7
1 5 2 7 3
"""