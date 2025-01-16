# HW - 1 - Nested List - Easy to Medium - Swap 2 columns

def read_list_of_list():
    rows = int(input())
    list_of_list = [list(map(int, input().split())) for _ in range(rows)]
    old_c, new_c = map(int, input().split())
    for i in range(len(list_of_list)):
        list_of_list[i][old_c], list_of_list[i][new_c] = list_of_list[i][new_c], list_of_list[i][old_c]
    return list_of_list

print(read_list_of_list())

"""
3
8 16 9 52
3 15 27 6
14 25 2 10
0 3

[[52, 16, 9, 8], [6, 15, 27, 3], [10, 25, 2, 14]]
"""