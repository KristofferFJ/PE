# QUADRATIC PRIMES: n**2 + a*n + b med |a|<1000 og |b|<=1000. Find det polynomium, der rammer flest primtal.

import timeit
start = timeit.default_timer()

# Primtalsliste
num = 10**7
primes = [True]*(num+1)
primes[0]=primes[1]=False
for i in range(2,int((num**.5))+1):
    ii = i**2
    if primes[i]:
        while ii <= num:
            primes[ii] = False
            ii += i


def primes_check(a,b):
    cons = 0
    prime = True
    i=-1
    while prime:
        i+=1
        if primes[i**2 + a*i + b] == False:
            prime = False
    return i


record = 0
coef = (1,1)
for i in range(-999,1000):
    for j in range(-1000,1001):
        if primes_check(i,j) > record:
            record = primes_check(i,j)
            coef = (i,j)

print(record)
print(coef)
print("Som har produktet %s" % (coef[0]*coef[1]))

print(timeit.default_timer() - start)