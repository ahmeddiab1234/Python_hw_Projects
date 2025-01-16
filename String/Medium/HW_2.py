# HW - 2 - Medium - String - Compressing

def compressing():
    str1 = input()
    n = len(str1)
    if n == 1:
        return str1

    groups = []
    cnt = 1

    for i in range(1, n):
        if str1[i] == str1[i - 1]:
            cnt += 1
        else:
            groups.append((cnt, str1[i - 1]))
            cnt = 1
    groups.append((cnt, str1[-1]))  # Append the last group

    groups.sort(key=lambda x: (-x[0], x[1]))  # Sort by frequency (desc), then letter (asc)

    res = []
    for count, char in groups:
        if count > 1:
            res.append(f"{count}{char}")
        else:
            res.append(char)

    return "_".join(res)

print(compressing())


"""
aaabbbccc ⇒ 3a_3b_3c
z ⇒ z
aabbbbbddddcccc ⇒ 5b_4c_4d_2a
aabbccaa ⇒ 2a_2a_2b_2c
"""
