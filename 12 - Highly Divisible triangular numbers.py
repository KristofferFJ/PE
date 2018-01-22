import timeit
import math

start = timeit.default_timer()

num = 10

def t_divisors(n):
	div = 0
	i = 1
	j = 2
	while div < n:
		div = 0
		for k in range(1,int(math.sqrt(i))+1):
			if i % k == 0:
				div += 2
		print ("%s har %s divisorer" % (i,div))
		i += j
		j += 1
	return div

print (t_divisors(500))

stop = timeit.default_timer()
print (stop - start)