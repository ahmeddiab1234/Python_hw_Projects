# HW - 5 - Recursion - Medium - Is Palindrome

def is_palindrom(lst, start, end):
    if len(lst) == 0:
        return True
    if start== len(lst)//2:
        return True
    if lst[start] != lst[end]:
        return False
    return is_palindrom(lst, start+1,end-1)



if __name__ == '__main__':
    # lst = [1, 3, 5, 7, 4, 2]
    tests = [[], [5], [5, 7], [5, 5], [1, 2, 3, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 3, 4, 2, 1]]
    for lst in tests:
        print(is_palindrom(lst,0,len(lst)-1))

"""
[] => true
[5] => true
[5, 7] => false
[5, 5] => true
[1, 2, 3, 2, 1] => true
[1, 2, 3, 3, 2, 1] => true
[1, 2, 3, 4, 2, 1]] => false

"""
