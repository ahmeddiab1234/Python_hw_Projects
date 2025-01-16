# HW - 3 - Easy to Medium - String - Grouping

def grouping(string):
    lst = []
    group = string[0]
    for i in range(1, len(string)):
        if string[i].lower() == string[i - 1].lower():
            group += string[i]
        else:
            lst.append(group)
            group = string[i]
    lst.append(group)
    return ','.join(lst)

print(grouping('111222aabbb'))
print(grouping('HHHH'))
print(grouping('5'))
print(grouping('abcdddddeefa'))
print(grouping('abcdDdDdeEfa'))

"""
111222aabbb ⇒ 111,222,aa,bbb
HHHH ⇒ HHHH
5 ⇒ 5
abcdddddeefa ⇒ a,b,c,ddddd,ee,f,a
abcdDdDdeEfa ⇒ a,b,c,dDdDd,eE,f,a
"""
