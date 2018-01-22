import timeit
start = timeit.default_timer()

num = 2 * 10^6

primes = [True] * (num)

def find_primes(list):
	for i in range(2,num):
		n = 2
		while i * n <= len(list)-1:
			primes[i*n] = False
			n += 1
	return primes

find_primes(primes)

def sum_primes(list):
	sum = 0
	for i in range(2,len(list)):
		if list[i]:
			sum += i
	return sum

print (sum_primes(primes))

stop = timeit.default_timer()
print (stop - start)
