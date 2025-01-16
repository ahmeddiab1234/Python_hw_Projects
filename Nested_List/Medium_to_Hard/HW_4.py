# HW - 4 - Medium to Hard - Nested List - Greedy Robot

def read_matrix():
    rows = int(input())
    assert rows > 0
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    return rows, len(matrix[0]), matrix

def ropot():
    rows, cols, matrix = read_matrix()
    i, j = 0, 0
    total_value = matrix[0][0]
    
    while i < rows - 1 or j < cols - 1:
        next_moves = []
        if j + 1 < cols:
            next_moves.append((matrix[i][j + 1], i, j + 1))
        if i + 1 < rows:
            next_moves.append((matrix[i + 1][j], i + 1, j))
        if i + 1 < rows and j + 1 < cols:
            next_moves.append((matrix[i + 1][j + 1], i + 1, j + 1))
        
        if not next_moves:
            break
        
        max_val, ni, nj = max(next_moves) 
        total_value += max_val
        i, j = ni, nj 

    return total_value

print(ropot())



"""
3
1 2 3
4 5 6
7 8 9
⇒ (0, 0) (1, 1), (2, 2) ⇒ 15
3
1 2 3
5 4 9
7 6 8
⇒ (0,0)⇒(1,0)⇒(2,0)⇒(2,1)⇒(2,2)
⇒27

2
1 2 3 4 5
6 7 8 9 10
⇒ 35
"""
