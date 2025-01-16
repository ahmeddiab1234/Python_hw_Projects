# HW - 6 - Medium to Hard - Nested List - Matrix pretty print

def matrix_pretty_print():
    row = int(input())
    matrix = []
    for _ in range(row):
        matrix.append(input().split())
    for i in range(row):
        max_len = max(len(val) for row in matrix for val in row)
        for j in range(row):
            print(matrix[i][j].ljust(max_len),end='')
            if(j!=row-1):
                print( ' # ', end='')
        print()


matrix_pretty_print()
def matrix_pretty_print():
    row = int(input())
    matrix = []
    for _ in range(row):
        matrix.append(input().split())
    
    col_lengths = [max(len(matrix[i][j]) for i in range(row)) for j in range(len(matrix[0]))]

    for i in range(row):
        for j in range(len(matrix[0])):
            print(matrix[i][j].ljust(col_lengths[j]), end='')
            if j != len(matrix[0]) - 1:
                print(' # ', end='')
        print()

matrix_pretty_print()

"""
3
mostafa saad ibrahim
hey woooooooow me
xx OK kkkkkkkkkkkk

mostafa # saad       # ibrahim
hey     # woooooooow # me
xx      # OK         # kkkkkkkkkkkk
"""