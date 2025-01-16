# HW - 4 - Nested List - Easy to Medium - Max value

def find_max_pos():
    rows = int(input())
    list_of_list = [list(map(int, input().split())) for _ in range(rows)]
    max_row_pos,max_col_pos = -1,-1
    max_val = list_of_list[0][0]
    for i in range(rows):
        for j in range(len(list_of_list[0])):
            if max_val <= list_of_list[i][j]:
                max_val = list_of_list[i][j]
                max_row_pos,max_col_pos = i,j

    print(f'Max value at position ({max_row_pos}, {max_col_pos}) with value =  {max_val} ')

find_max_pos()

"""
3
1 5 1 10
2 10 3 4
1 10 10 7
Max value at position (2, 2) with value = 10
"""