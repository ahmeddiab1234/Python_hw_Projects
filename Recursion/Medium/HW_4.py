# HW - 4 - Recursion - Medium - right-Max

def right_max(lst, idx=0):
    if idx == len(lst)-1:
        return [lst[idx]]
    tail = right_max(lst, idx + 1)
    return [max(lst[idx], tail[0])] + tail

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 4, 2]
    print(right_max(lst)) # [7, 7, 7, 7, 4, 2]

