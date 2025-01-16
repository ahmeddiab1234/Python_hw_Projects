# HW - 4 - More Functions - Map 

def myMap(func, *iterable): 
    res = [ func(*args) for args in zip(*iterable)]
    return res

def multible_abs(a, b, c):
    return abs(a) * abs(b) * abs(c)

res = myMap(multible_abs, [1, -2, 3, 2], [-4, 5, 6, 7], [4, -5, -10, 9, 11])

print(res) # [16, 50, 180, 126]
