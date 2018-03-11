# ALMINDELIGE FUNKTIONER


def factors(n):
    factors = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                factors.append(i)
                break
    return factors


def primes(n):
    primes_bool = [True]*(n+1)
    primes_bool[0] = primes_bool[1] = False
    for i in range(2, int(n**.5)):
        ii = i*i
        while ii <= n:
            primes_bool[ii] = False
            ii += i
    return primes_bool


def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*fact(n-1)


def anagram(n, m):
    a,b = str(n), str(m)
    value = True
    for i in range(10):
        if a.count(str(i)) != b.count(str(i)):
            value = False
    return value


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
