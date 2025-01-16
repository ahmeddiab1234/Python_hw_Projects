# HW - 1 - String - Easy to Medium - Is Palindrome?

def is_palindrome(s):
    n = len(s)
    if n <= 1:
        return True
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

print(is_palindrome("madam")) # True
print(is_palindrome("racecar")) # True
print(is_palindrome("11/11/11")) # True
print(is_palindrome("12321"))    # True
print(is_palindrome("ahmeddiab")) # False
print(is_palindrome("1233245")) # False

"""
E.g. madam, racecar, 11/11/11, 12321
"""
