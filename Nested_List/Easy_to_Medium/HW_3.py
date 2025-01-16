# HW - 3 - Nested List - Easy to Medium - Filter empty rows

def filter_empty_rows():
    rows = int(input())
    list_of_list = [list(map(int, input().split())) for _ in range(rows)]
    new_list = [ i   for i in list_of_list  if len(i)>0]

    return new_list
print(filter_empty_rows())

"""
5
1 2 3

4 5

6

[[1, 2, 3], [4, 5], [6]]
"""
