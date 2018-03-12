#60 - Prime pair sets
"""
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. The s of these four primes, 792, represents the lowest s for a set of four
primes with this property.

Find the lowest s for a set of five primes for which any two primes concatenate to produce another prime.
"""
import time
from sympy import sieve

primes = list(sieve.primerange(1, 10**8))

# Primes can't end in 2 or 5.
primes.remove(2) 
primes.remove(5)


def prime_pair_set(arr):
    set = True
    array = [str(a) for a in arr]
    if len(arr) == 1:
        return True
    else:
        for i in range(len(array)):
            for j in range(i + 1, len(arr)):
                if not ((int(array[i] + array[j]) in sieve) and (int(array[j] + array[i]) in sieve)):
                    set = False
                    print (str(arr) + " BUM")
                    return set
        return set


input("Klar til at starte?")

min = 10**12
max = 200
for p_1 in range(1, 500):
    print ("p_1 er " + str(primes[p_1]))
    for p_2 in range(p_1 + 1, 1224):
        if not prime_pair_set([primes[p_1], primes[p_2]]):
            continue
        for p_3 in range(p_2 + 1, 1225):
            if not prime_pair_set([primes[p_1], primes[p_2], primes[p_3]]):
                continue
            for p_4 in range(p_3 + 1, 1226):
                if not prime_pair_set([primes[p_1], primes[p_2], primes[p_3], primes[p_4]]):
                    continue
                for p_5 in range(p_4 + 1, 1227):
                    if prime_pair_set([primes[p_1], primes[p_2], primes[p_3], primes[p_4], primes[p_5]]):
                        print ("Succes ved " + str([primes[p_1], primes[p_2], primes[p_3], primes[p_4], primes[p_5]]))
                        time.sleep(5)
                        input("Noget er fundet")
                        if min > primes[p_1] + primes[p_2] + primes[p_3] + primes[p_4] + primes[p_5]:
                            min = primes[p_1] + primes[p_2] + primes[p_3] + primes[p_4] + primes[p_5]