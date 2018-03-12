# DISTINCT PRIME FACTORS: Find de første 4 på hinanden følgende tal,
# der har 4 forskellige primdivisorer.

import timeit
start = timeit.default_timer()


def factorize(n):
    primes = set([])
    while n != 1:
        for i in range(2,n+1):
            if n % i == 0:
                n = n // i
                primes.add(i)
                break
    return primes


conc = 4
count = 0
for i in range(500,10**7):
    if count == conc:
        print ("Found at "+str(i-conc))
        break
    elif len(factorize(i)) == conc:
        count += 1
    else:
        count = 0

print (timeit.default_timer() - start)