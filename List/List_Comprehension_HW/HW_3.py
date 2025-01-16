# HW - 3 - Slicing and List Comprehension - Fixed sliding window

def max_sum_sublist(lst, k):
    n = len(lst)
    if k > n:
        return "Invalid input: "
    
    max_sum = float('-inf')
    current_sum = sum(lst[:k]) 
    start_index = 0

    for i in range(k, n):
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i - k + 1
        current_sum += lst[i] - lst[i - k]

    return f"Starts at {start_index} with Sum {max_sum}"

lst1 = [1, 0, 3, -4, 2, -6, 9]
k1 = 3
print(max_sum_sublist(lst1, k1))

lst2 = [30, -6, -8, 10, 2]
k2 = 4
print(max_sum_sublist(lst2, k2))


"""
1 0 3 -4 2 -6 9
3
Output: Starts at 4 with Sum 5
30 -6 -8 10 2
4
"""