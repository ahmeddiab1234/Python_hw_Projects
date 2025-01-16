# HW - 1 - List - Medium to Hard - Find most frequent number

def freq_list(lst):
    offset = 500
    max_value = 270 + offset
    min_value = -500 + offset

    freq = [0] * (max_value - min_value + 1)

    for val in lst:
        freq[val + offset] += 1

    max_freq = max(freq)
    smallest_value = None

    for i in range(len(freq)):
        if freq[i] == max_freq:
            smallest_value = i - offset
            break

    return smallest_value, max_freq

lst = [-1, 2, -1, 3, -1, 5, 5]
value, count = freq_list(lst)
print(f"Value {value} repeated {count}")

"""
-1 2 -1 3 -1 5 5 ⇒ Value -1 repeated 3
"""