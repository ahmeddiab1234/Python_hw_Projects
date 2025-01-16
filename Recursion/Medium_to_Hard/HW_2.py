# HW - 1 - Medium to Hard - Recursion - cout primes

def read_matrix():
    row = int(input())
    if row <= 0:
        raise ValueError('The rows must be greater than 0.')
    matrix = []
    for _ in range(row):
        row_values = list(map(int, input().split()))
        if matrix and len(row_values) != len(matrix[0]):
            raise ValueError('All rows must have the same number of columns.')
        matrix.append(row_values)
    return row, len(matrix[0]), matrix

def is_grid_valid(r, c, row, col):
    return 0 <= r < row and 0 <= c < col

def get_positions(r, c, row, col):
    directions = [(1, 0), (0, 1), (1, 1)]
    return [(r + di, c + dj) for di, dj in directions if is_grid_valid(r + di, c + dj, row, col)]

def get_path_sum(matrix, r=0, c=0):
    res = matrix[r][c]
    rows, cols = len(matrix), len(matrix[0])
    positions = get_positions(r, c, rows, cols)

    if not positions:
        return res

    r, c = max(positions, key=lambda pos: matrix[pos[0]][pos[1]])
    res += get_path_sum(matrix, r, c)
    return res

if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    print(get_path_sum(matrix))


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
