# HW - 1 - Dictionary - Medium to Hard - Special String Mapping

def special_string(string):
    dict1 = {}
    for key,val in zip('abcdefghijklmnopqrstuvwxyz0123456789','YZIMNESTODUAPWXHQFBRJKCGVL!@#$%^&*()'):
        dict1[key] = val
    res = []
    for char in string:
        if char in dict1.keys():
            res.append(dict1[char])
        else:
            res.append(char)
    print(''.join(res))


special_string('acMNmn39')
special_string('vwXYZ0123')

"""
abcdefghijklmnopqrstuvwxyz
YZIMNESTODUAPWXHQFBRJKCGVL

0123456789
!@#$%^&*()

acMNmn39 ⇒ YIMNPW$)
vwXYZ0123 ⇒ KCXYZ!@#$
"""