# HW - 1 - Medium to Hard - Recursion - cout primes

def is_prime(val, cnt=3):
    if val == 2:
        return True
    if val < 0 or val%2==0:
        return False 
    if val == cnt:
        return True
    if val % cnt ==0:
        return False
    return is_prime(val, cnt+2)

def count_primes(start, end):
    if start > end:
        return 0 
    cnt = is_prime(start)
    cnt = cnt + count_primes(start+1, end) 
    return cnt   

if __name__ == '__main__':
    print(count_primes(10, 20))
    print(count_primes(10, 200))
