# Prime digit replacements
# Vi skal bytte cifre fra et primtal ud med 2 ens tal og det skal så give 8 primtal.
# Vi bytter altså ud med 0,0, 1,1, 2,2 o.s.v.

# Bytte ud svarer til at lægge noget til. Siden 3 går op i mindst 3 af dem hvis det
# vi lægger til ikke er 0 modulo 3, må det nødvendigvis være 0 modulo 3.

# 1-cifret dur ikke da vi kun kan lægge 10^x'ere til og de er 1 modulo 3.
# Samme gælder med 2-cifret udover at vi kommer til at lægge 2 modulo 3 til.
# 3 cifre kan vi fjerne som vi har lyst.

# Vi fjerner ikke det første ciffer, da vi i så fald får alt for mange lige tal.

# At "udskifte" tal svarer til at lægge til.

import time

num = 10**8
primes = [True] * (num+1)
primes[0]=primes[1]=False
for i in range(2, int(num**.5)+1):
    ii = i*i
    while ii <= num:
        primes[ii] = False
        ii += i

primes_list = []
for i in range(2,num):
    if primes[i]:
        primes_list.append(i)

def check(n):
    for i in range(0,3):
        j = str(i)
        if str(n).count(j) == 3:
            plus = 0
            prime_count = 0
            for k in range(len(str(n))):
                if str(n)[-1-k] == j:
                    plus += 10**k
            for l in range(1,10):
                if primes[n+plus*l] and len(str(n+plus*l)) == len(str(n)):
                    prime_count += 1
            if prime_count > 6:
                print ("Ved %s fandt vi %s primtal" % (n,prime_count+1))
                time.sleep(3)


for prime in primes_list:
    check(prime)