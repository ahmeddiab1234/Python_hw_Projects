# HW - 7 - List - Easy to Medium - Find the 3 minumn values

def smallest_3_val(lst):
    res = []
    if len(lst) < 1:
        return lst

    for i in lst:
        res.append(i)
        if len(res) > 3:
            res.sort()
            res.pop()
    res.sort()
    return res

lst1 = [4, 1, 3, 10, 8]
print(smallest_3_val(lst1))
lst2 = [7, 9, -2]
print(smallest_3_val(lst2))
lst3 = [1, -5]
print(smallest_3_val(lst3))

"""
4 1 3 10 8 ⇒ 1 3 4
7 9 -2 ⇒ -2 7 9
1 -5 ⇒ -5 1
"""