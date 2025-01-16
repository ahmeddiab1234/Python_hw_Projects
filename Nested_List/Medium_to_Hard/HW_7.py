# HW - 7 - Medium to Hard - Nested List - How many primes

def list_relations(depth=3, rows=4, cols=5):
    idx=0
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                print(f'{d}, {r}, {c} ==> {idx}')
                idx+=1
# list_relations()

depth, rows, cols, choose, *remain = map(int, input().split())

depth_block = rows * cols
row_block = cols
col_block = 1

if choose ==1:
    d, r, c = remain
    idx = d * depth_block + r * row_block + c * col_block
    print(idx)
else:
    idx = remain[0]
    d = idx // depth_block
    r = (idx % depth_block) // row_block
    c = (idx % depth_block) % row_block
    print(d, r, c)

"""
3 4 5   1    1 0 0 => 20
3 4 5   2    20 => 1 0 0 
3 4 5   1    1 1 1 => 26
3 4 5   1    2 3 2 => 57
3 4 5   1    2 0 0 => 40
3 4 5   2    59 => 2 3 4
"""