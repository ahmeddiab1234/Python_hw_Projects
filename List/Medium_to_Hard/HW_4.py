# HW - 2 - List - Medium to Hard - Recamán's sequence

def find_recaman(num):
    lst = [0] * 201
    seen = {0}
    for idx in range(1, 201):
        val1 = lst[idx - 1] - idx
        if val1 > 0 and val1 not in seen:
            lst[idx] = val1
        else:
            lst[idx] = lst[idx - 1] + idx
        seen.add(lst[idx])
    return lst[num]

print(find_recaman(6))  # 13
print(find_recaman(9))  # 21
print(find_recaman(17))  # 25


"""
The series is: 0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43
"""