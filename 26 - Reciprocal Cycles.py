#RECIPROCAL CYCLES
#1/3 har en cycle på 1 fordi 3 | 10**1 - 1. Se:
#9/3 = 3 => 10/3 = 3,3333 => 1/3 = 0,33333
#1/7 har en cycle på 6 for 7 | 10**6 - 1. Se:
#(10**6-1)/7 = 142857 så 10**6/7 = 142857 + 1/7 så 1/7 = 0,142857-1/7.

import timeit

start = timeit.default_timer()

def cycle_len(n):
	found = False
	i = 0
	if n%2==0 or n%5==0:
		return 0
	while not found:
		i+=1
		if (10**i - 1)%n==0:
			found = True
	return i

def max_cycle(n):
	max = 1
	for i in range(2,n):
		if cycle_len(i) > max:
			max = i
	return max

print (max_cycle(1000))
print (timeit.default_timer() - start)