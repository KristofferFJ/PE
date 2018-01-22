import timeit
start = timeit.default_timer()

def collatz_sequence(n):
	sequence = [n]
	while n != 1:
		if n % 2 == 0:
			n = n // 2
			sequence.append(n)
		else:
			n = 3 * n + 1
			sequence.append(n)
	return sequence

def largest_sequence(n):
	max = []
	num = 1
	for i in range(1,n):
		if len(collatz_sequence(i)) > len(max):
			max = collatz_sequence(i)
			num = i
			print ("Ny rekord ved %s med en længde på %s" % (i, len(max)))
	return i, max
	print (max)

print (largest_sequence(1000000))

stop = timeit.default_timer()
print (stop - start)