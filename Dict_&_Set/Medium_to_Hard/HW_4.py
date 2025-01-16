# HW - 4 - Dictionary - Medium to Hard - Filter Duplicates:

def filter_duplicates_preserve_order(lst):
    dict1 = {}
    res = []
    for i in lst:
        t = tuple(i)
        if t not in dict1:
            dict1[t] = 1
            res.append(i)
    return res

print(filter_duplicates_preserve_order([[7, 1], [2, 4], [7, 1], [5, 2], [2, 4]]))

"""
lst = [ [7, 1], [2, 4], [7, 1], [5, 2], [2, 4] ]
output = [ [7, 1], [2, 4], [5, 2] ]
"""
