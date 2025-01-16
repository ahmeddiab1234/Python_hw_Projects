# HW - 6 - Medium to Hard - Recursion - Fibonacci

def fibonacci1(n):
    if n == 0 or n == 1:
        return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)


# optimized function
def fibonacci2(n):
    global res
    if len(res) == 0:
        res = [-1] * (n + 1)
        res[0] = 0
        res[1] = 1

    if res[n] == -1:
        res[n] = fibonacci2(n - 1) + fibonacci2(n - 2)
    return res[n]

if __name__ == '__main__':
    print(fibonacci1(30))
    print(fibonacci1(35))
    # print(fibonacci1(40))   # too late 

    res = []
    print(fibonacci2(30))
    res = []
    print(fibonacci2(35))
    res = []
    print(fibonacci2(40))
