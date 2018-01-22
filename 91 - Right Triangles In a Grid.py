import timeit
import math
from sympy import Symbol
start = timeit.default_timer()

def is_right(a,b,c,d):
	if a * c + b * d == 0 or (-a)*(c-a) + (-b)*(d-b) == 0 or (-c)*(a-c) + (-d)*(b-d) == 0:
		return True
	else:
		return False

def find_triangles(n):
	x1 = x2 = y1 = y2 = n
	count = 0
	while x1 + x2 + y1 + y2 > 0:
		if x1*y2 - x2*y1 != 0 and is_right(x1,x2,y1,y2):
			count += 1
		if x2 == x1 == 0:
			if y1 == 0:
				y1 = n
				y2 -= 1
			else:
				y1 -= 1
			x2 = y2
			x1 = y1
		elif x1 == 0:
			x1 = n
			x2 -= 1
		else:
			x1 -= 1
	return count
		
print(find_triangles(50))
		
stop = timeit.default_timer()
print (stop - start)