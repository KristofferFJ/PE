import timeit
import math
from sympy import Symbol
start = timeit.default_timer()

F = open("../../resources/99.txt", "r")

def log2(n,m):
	return m * math.log(n)

def compare():
	max = 0
	index = 0
	for line in F:	
		index += 1
		b = line.split(",")
		c = [int(e) for e in b]
		if log2(c[0],c[1]) > max:
			max = log2(c[0],c[1])
			best = line
			lineNumber = index

	return lineNumber


print (compare())

stop = timeit.default_timer()
print (stop - start)