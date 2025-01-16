# HW - 6 - Slicing and List Comprehension - longest sublist

def longest_sublist(lst):
    for idx in range(len(lst)):
        if lst[idx]==0:
            lst[idx] = -1
    res = []
    for idx1 in range(len(lst)):
        sum=0
        for idx2 in range(idx1,len(lst)):
            sum+=lst[idx2]
            if sum==0:
                res.append(abs(idx2-idx1) +1)
    max_res = 0
    if len(res) :
        max_res = max(res)
    return max_res

print(longest_sublist([1, 0, 0, 0, 1, 1, 1]))
print(longest_sublist([1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]))
print(longest_sublist([1, 1, 1, 1]))
print(longest_sublist([1, 1, 1, 0, 0]))
print(longest_sublist([0]))


"""
1 0 0 0 1 1 1 ⇒ 6 (e.g. 100011 or 000111)
1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 0 1 ⇒ 8 (e.g. 00101101)
1 1 1 1 ⇒ 0
1 1 1 0 0 ⇒ 4
0 ⇒ 0
"""