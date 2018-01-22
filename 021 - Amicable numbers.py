import timeit

start = timeit.default_timer()

def divisor_sum(n):
	sum = 0
	for i in range(1,n):
		if n % i == 0:
			sum += i
	return sum

def amicable(n):
	if divisor_sum(n) != n:
		if divisor_sum(divisor_sum(n)) == n:
			return True
		else:
			return False
	else:
		return False

sum = 0		
for i in (range(10000)):
	if amicable(i):
		sum += i

print (sum)
		
print (timeit.default_timer() - start)