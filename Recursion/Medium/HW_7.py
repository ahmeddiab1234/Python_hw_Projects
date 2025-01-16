# HW - 7 - Recursion - Medium - Trace The Code

def do_somethin1(n):
    if n:
        print(n%10, end='')
        do_somethin1(n//10)

def do_something2(n):
    if n:
        print(n%10, end='')
        do_something2(n//10)

if __name__ == '__main__':
    do_somethin1(12345)
    print()
    do_something2(54321)
    do_something2(0)


"""
this functions trace the number and  print it reversed 
when we take the mdoulas by 10 for the number it will out the last num 
and when we take the floating devision it will remove tha last and out the remaining num

The output should be:
-------------
54321

12345
-------------
as 0 will be false it will not enter the recursion fun and will out from the fun
"""