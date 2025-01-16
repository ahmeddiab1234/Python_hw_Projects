# HW - 2 - Dictionary - Medium to Hard - Sort by type

def sort_different_types(lst):
    dict1 = {}
    for l in lst:
        ty = type(l)
        dict1.setdefault(ty,[])
        dict1[ty].append(l)
    
    for val in dict1.values():
        val.sort()
    res = [ val for val in dict1.values()]
    return res
    

lst = [10, 'most', 2.5, 7, 'aly', 9, 4.5, 2, 'ziad', -4, 1.1, [1, 5], 5, [0, 7, 8]]
output = sort_different_types(lst)
print(output)

"""
lst = [10, 'most', 2.5, 7, 'aly', 9, 4.5, 2, 'ziad', -4, 1.1, [1, 5], 5, [0, 7, 8]]
output = [-4, 2, 5, 7, 9, 10, 'aly', 'most', 'ziad', 1.1, 2.5, [0, 7, 8], [1, 5]]
"""