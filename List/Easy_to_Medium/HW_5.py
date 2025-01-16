# HW - 5 - List - Easy to Medium - Unique Numbers of ordered

def unique_ordered(lst):
    max_num = max(lst) + 1
    freq = [0] * max_num
    for i in lst:
        freq[i] += 1
    for i in lst:
        if freq[i] > 0:
            print(i, end=' ')
            freq[i] = 0

lst1 = [1, 1, 2, 2, 2, 5, 6, 6, 7, 8, 9, 9]
unique_ordered(lst1)

"""
intpu: 1 1 2 2 2 5 6 6 7 8 9 9
output: 1 2 5 6 7 8 9
"""
