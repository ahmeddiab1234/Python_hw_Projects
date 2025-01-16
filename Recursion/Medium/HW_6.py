# HW - 6 - Recursion - Medium - Is Palindrome

def start_with(string, sub_str, idx=0):
    if len(sub_str) == 0:
        return True
    if idx==len(sub_str):
        return True
    if len(sub_str) > len(string):
        return False
    if string[idx] != sub_str[idx]:
        return False
    return start_with(string, sub_str, idx+1)


if __name__ == '__main__':
    print(start_with("", "")) # True
    print(start_with("abcdefg", "")) # True
    print(start_with("abcdefg", "abcd")) # True
    print(start_with("abcdefg", "ax")) # False
    print(start_with("abcd", "abcdefg")) # False
    print(start_with("abcd", "abcd")) # True
