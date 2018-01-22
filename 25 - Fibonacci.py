import timeit
start = timeit.default_timer()

def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_list():
	sum1 = 1
	sum2 = 1
	count = 2
	while len(str(sum1)) < 1000:
		temp = sum1
		sum1 = sum1 + sum2
		sum2 = temp
		count += 1
	return count
	
print (fibonacci_list())

print (timeit.default_timer() - start)