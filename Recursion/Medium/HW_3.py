# HW - 3 - Recursion - Medium - Left-Max

def left_max(lst):
    if len(lst) <= 1:
        return lst
    head = left_max(lst[:-1])
    tail = max(head[-1], lst[-1])
    head.append(tail)
    return head

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 4, 2]
    print(left_max(lst)) # [1, 3, 5, 7, 7, 7]