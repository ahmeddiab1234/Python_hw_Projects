# HW - 2 - List - Medium to Hard - Digits frequency

def digit_freq(lst):
    freq = [0] * (9+1)
    for num in lst:
        for val in str(num):
            val = int(val)
            freq[val] +=1

    for idx in range(0,10):
        print(idx, freq[idx])    

lst = [78, 307]
digit_freq(lst)


"""
Input 78 307
Output:
0 1
1 0 
2 0
3 1
4 0
5 0
6 0
7 2 
8 1
9 0
"""