# HW - 1 - Hard - While Loop - Find NOs

N = int(input())
while N > 0:
    str_no = input()
    if len(str_no) == 2 and ((str_no[0].lower() == 'n' and str_no[1].lower() == 'o') or (str_no[0].lower() == 'o' and str_no[1].lower() == 'n')):
        print(f'Match: {str_no}')
    N -= 1

    
"""
9
Yss
No
    Match: NO
noOO
oN
    Match: oN
Mostafa
no
    Match: no
nN
oOOooo
oO
"""