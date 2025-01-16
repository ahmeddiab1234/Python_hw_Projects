# HW - 6 - Slicing and List Comprehension - Josephus problem


def find_Josephus_winner(n, k):
    res = []
    list_killed = list(range(1, n + 1))
    last_index = 0

    while len(list_killed) > 1:
        last_index = (last_index + k - 1) % len(list_killed)
        res.append(list_killed.pop(last_index))
    
    res.append(list_killed[0])
    return res

# Test cases
print(* find_Josephus_winner(7, 1))
print(*find_Josephus_winner(7, 2))
print(*find_Josephus_winner(7, 3))
print(*find_Josephus_winner(7, 4))
print(*find_Josephus_winner(7, 5))
print(*find_Josephus_winner(7, 6))
print(*find_Josephus_winner(7, 7))
print(*find_Josephus_winner(7, 14))
print(*find_Josephus_winner(7, 1000))
print(*find_Josephus_winner(7, 99999))


"""
7 1 ⇒ 1 2 3 4 5 6 7
7 2 ⇒ 2 4 6 1 5 3 7
7 3 ⇒ 3 6 2 7 5 1 4
7 4 ⇒ 4 1 6 5 7 3 2
7 5 ⇒ 5 3 2 4 7 1 6
7 6 ⇒ 6 5 7 2 1 4 3
7 7 ⇒ 7 1 3 6 2 4 5
7 14 ⇒ 7 2 6 3 5 4 1
7 1000 ⇒ 6 3 2 1 4 7 5
7 99999 ⇒ 4 7 5 2 1 3 6
"""