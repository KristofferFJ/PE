# FIND DET MINDSTE TAL DER KAN DIVIDERES AF ALLE TALLENE OP TIL
import timeit
n = int(input("MFM for tallet "))

start = timeit.default_timer()


def factorize(n):
    primes = []
    while n != 1:
        for i in range(2,n+1):
            if n % i == 0:
                n = n // i
                primes.append(i)
                break
    return primes


def lcm(n):
    factors = []
    prod = 1
    for i in range(2,n+1):
        primes = factorize(i)
        print ("Faktorerne er ved %s, %s" % (i-1, factors))
        for j in range(2,n+1):
            while primes.count(j) > factors.count(j):
                factors.append(j)
    for item in factors:
        prod *= item
    return prod


stop = timeit.default_timer()
print(lcm(n))
print(stop - start)