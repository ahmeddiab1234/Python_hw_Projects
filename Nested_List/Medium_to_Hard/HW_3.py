# HW - 3 - Medium to Hard - Nested List - How many primes

def read_matrix():
    rows = int(input())
    assert rows > 0
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    cols = len(matrix[0])
    return rows, cols, matrix

def is_prime(val):
    if val < 2:
        return False
    if val == 2:
        return True
    if val % 2 == 0:
        return False
    for i in range(3, int(val**0.5) + 1, 2):
        if val % i == 0:
            return False
    return True

def how_many_prime():
    rows, cols, matrix = read_matrix()
    queries = int(input())
    results = []
    
    for _ in range(queries):
        sr, sj, r, c = map(int, input().split())
        assert 0 <= sr < rows and 0 <= sj < cols
        assert sr + r <= rows and sj + c <= cols
        
        cnt = 0
        for i in range(sr, sr + r):
            for j in range(sj, sj + c):
                if is_prime(matrix[i][j]):
                    cnt += 1
        results.append(cnt)
    
    for result in results:
        print(result)

how_many_prime()
"""
3
8 2 9 5
3 2 27 6
7 8 29 22
2
1 0 2 2
0 1 2 3

3
3
"""
