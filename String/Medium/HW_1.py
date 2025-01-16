# HW - 1 - Medium - String - Filtering

def filtering():
    string1 = input()
    res=[]
    char =  ''
    for c in string1:
        if c == ',' or c==' 'or c == '$' or c == '#':
           if char:
                res.append(char)
                char=''
        else:
            char+=c
    if char:
        res.append(char)
    res.sort()
    return res

print(filtering())

"""
apple,banana, , , apple,student### #student$$apple

['apple', 'apple', 'apple', 'banana', 'student', 'student']
"""