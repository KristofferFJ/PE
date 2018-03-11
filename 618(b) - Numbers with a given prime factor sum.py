#618 - Numbers with a given prime factor s
import sys
import math

sys.setrecursionlimit(5000)

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
    return s(factors)
	
primes_bool = [True for i in range(75025)]
primes_bool[0] = False
primes_bool[1] = False
for i in range(2,int(len(primes_bool)**0.5)):
	if primes_bool[i]:
		j = i*i
		while j < len(primes_bool):
			primes_bool[j] = False
			j += i
primes = []
for i in range(len(primes_bool)):
	if primes_bool[i]:
		primes.append(i)
		


def f(l, N):
	a = [1]+[0]*N
	for i in l:
		for j in range(N-i+1):
			a[i+j] += a[j]
			print (a)
	return a[-1]

print (f([2,3,5],11))  

"""	
total = 0
for i in range(2,25):
	print ("tjekker "+str(i))
	total += finder(fib(i))
	
"""