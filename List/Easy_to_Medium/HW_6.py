# HW - 6 - List - Easy to Medium - Smallest pair

def small_lst(lst):
    mn_val = float('inf')
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if mn_val > lst[i] + lst[j] - i + j:
                mn_val = lst[i] + lst[j] - i + j
    return mn_val

lst1 = [20, 1, 9, 4]
print(small_lst(lst1))

"""
20 1 9 4 ⇒ 7
"""