# HW - 6 - Nested List - Easy to Medium - Value in first column

def val_in_fir_col():
    rows = int(input())
    list_of_list = [list(map(int, input().split())) for _ in range(rows)]
    col = int(input())

    for row in list_of_list:
        if col in row:
            print(f'found in col {row.index(col)}')
            break
    else:
        print('not found')

val_in_fir_col()


"""
3
8 16 9 52
3 15 15 6
14 25 2 10
15

found in col 1
"""