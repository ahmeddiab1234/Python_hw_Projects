# HW - 3 - List - Easy to Medium - Search for a number

def search(lst, num):
    cnt = -1
    for i in range(len(lst)):
        if lst[i] == num:
            cnt = i
    print("Query " + str(num) + " Answer " + str(cnt))

lst1 = [1, 2, 7, 3, 7]
query = [7, 9, 2]

for i in range(len(query)):
    search(lst1, query[i])

