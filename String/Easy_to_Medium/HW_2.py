# HW - 2 - Easy to Medium - String - Convert to number

def our_int(string):
    res = 0
    num = '0123456789'
    for i in string:
        res = res *10 + num.find(i)
    return res, res*3

print(our_int('100')) # 100 300
print(our_int('0000200')) # 200 600

"""
“100” ⇒ 100 300
“0000200” ⇒ 200 600
"""