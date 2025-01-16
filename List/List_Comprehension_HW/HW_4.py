# HW - 3 - Slicing and List Comprehension - Count increasing sublists

def count_inc(lst):
    cnt = 0
    for i in range(len(lst)):
        cnt += sum(all(lst[k] < lst[k + 1] for k in range(i, j - 1)) for j in range(i + 1, len(lst) + 1))
    return cnt

lst1 = [1, 2, 3, 4]
print(count_inc(lst1))

lst2 = [4, 3, 2, 1]
print(count_inc(lst2))

lst3 = [10, 20, 1, 5]
print(count_inc(lst3))



"""
1 2 3 4 ⇒ 10
4 3 2 1 ⇒ 4 
10 20 1 5 ⇒ 6
"""

