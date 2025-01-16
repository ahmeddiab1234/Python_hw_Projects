# HW - 1- Recursion - Easy to Medium - Length of 3n+1

def length_3n_plus_1(n):
    if n==1:
        return 1
    if n%2==0:
        return 1 + length_3n_plus_1(n//2)
    else:
        return 1 + length_3n_plus_1(3*n+1)



print(length_3n_plus_1(6)) # ⇒ 9

