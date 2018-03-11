# 618 - Numbers with a given prime factor s
# from math import *


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def prime_factors_s(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return (factors)


def finder(s):
    list = []
    for i in range(1,(int(s/2)+1)**2):
        if prime_factors_s(i) == s:
            list.append(i)
    return (list)


total = 0
for i in range(2,25):
    print("tjekker "+str(i))
    total += finder(fib(i))
