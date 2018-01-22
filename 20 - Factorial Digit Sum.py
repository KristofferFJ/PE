import timeit
import math
from sympy import Symbol
start = timeit.default_timer()

def factorial(n):
	prod = 1
	for i in range(1,n+1):
		prod *= i
	return prod

def digit_sum(n):
	sum = 0
	while n:
		sum += n % 10
		n //= 10
	return sum

print (digit_sum(factorial(10)))
print (digit_sum(factorial(100)))

stop = timeit.default_timer()
print (stop - start)