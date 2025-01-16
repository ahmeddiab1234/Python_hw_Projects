# HW - 7 - Recursion - Easy to Medium - List Accumulation v1

def list_accumulate(lst, acc=0):
    if len(lst) == 0:
        return []
    new_sum = acc + lst[0]
    return [new_sum] + list_accumulate(lst[1:], new_sum)

print(list_accumulate([1, 8, 2, 10, 3]))  # Output: [1, 9, 11, 21, 24]
