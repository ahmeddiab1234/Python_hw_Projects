# HW - 1 - Easy to Medium - List - Is increasing array?


def is_increment(lst):
    for i in range(1,len(lst)):
        if lst[i]<lst[i-1]:
            return False
    return True

lst = [1, 0, 7, 8, 9]
if(is_increment(lst)):
    print("YES")
else :
    print("NO")


"""
1 2 2 5 ⇒ YES
1 0 7 8 9 ⇒ NO
-10 10 ⇒ YES
"""