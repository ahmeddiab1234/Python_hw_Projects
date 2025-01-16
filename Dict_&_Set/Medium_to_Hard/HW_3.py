# HW - 3 - Dictionary - Medium to Hard - Fast Prefix Finder

def fast_prefix():
    n = int(input())
    dict1 = {}
    for i in range(n):
        str1 = input()
        dict1[i]=(str1)

    q = int(input())
    for i in range(q):
        str2 = input()
        res = []
        for key,val in dict1.items():
            if str2 in val:
                res.append(val)
        if len(res) >0:
            print(f'{str2} Matches {res}')
        else:
            print('not found')

fast_prefix()

"""
5
Hey
Hello
Hi
Mostafa Saad
Mostafa Ziad

4
He
He matches ['Hey', 'Hello']

H
H  matches ['Hey', 'Hello', 'Hi']

Most
Most matces ['Mostafa Saad', Mostafa Ziad']

MOST
not found
"""