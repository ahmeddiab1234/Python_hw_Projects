# HW - 1 - Files - Medium - Max * Sum of a file


path = r'E:\Python_live\Python_HW\Files\Medium\data.txt'
lst = []

with open(path, 'r') as file:
    lines = file.readlines()
    lst = [abs(int(i)) for i in lines]
res = max(lst) * sum(lst)
print(res)


"""
10
20
-2
5
-5
-8
010
"""
