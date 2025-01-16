# HW - 5 - Nested List - Easy to Medium - Special print

def special_print():
    last_row, last_col, left_diag, right_diag = 0, 0, 0, 0
    rows = int(input())
    list_of_list = [list(map(int, input().split())) for _ in range(rows)]

    for i in range(rows):
        for j in range(len(list_of_list[0])):
            if i == rows-1:
                last_row += list_of_list[i][j]
            if j == len(list_of_list[0])-1:
                last_col += list_of_list[i][j]
            if i==j:
                left_diag += list_of_list[i][j]
            if i == rows-j:
                right_diag += list_of_list[i][j]
    return last_row, last_col, left_diag, right_diag

print(special_print())


"""
3
8 16 9 52
3 15 27 6
14 25 2 10

51 68 25 104 
"""