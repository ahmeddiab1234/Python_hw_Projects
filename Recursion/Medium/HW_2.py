# HW - 2 - Recursion - Medium - List Accumulation v2

def list_accomulate(lst, idx):
    if idx==0:
        return
    list_accomulate(lst, idx-1)
    lst[idx] += lst[idx-1]


if __name__ == '__main__':
    lst = [1, 8, 2, 10, 3]
    list_accomulate(lst, len(lst)-1)
    print(lst) # [1, 9, 11, 21, 24]

