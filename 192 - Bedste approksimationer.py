import timeit
import math
from sympy import Symbol
start = timeit.default_timer()

def gcd(x, y):
	while (y != 0):
		x, y = y, x % y
	return x

def simp(list):
	x = int(list[0])
	y = int(list[1])
	x //= gcd(x, y)
	y //= gcd(x, y)
	return [x, y]
	
def chain_to_dec(list):
		x = list[len(list)-1]
		for i in range(len(list)-1,0,-1):
			x = 1/x + list[i-1]
		return x

def dec_to_chain(num):
	x = num // 1
	return int(x)
		
def chain_to_frac(list):
	temp = 1
	x, y = 1, list[len(list)-1]
	for i in range(len(list)-1,0,-1):
		temp = x
		x = y
		y = list[i-1] * y + temp
		x, y = simp([x,y])[0], simp([x,y])[1]
	return [y, x]

def best_frac_below(num,limit):
	x = math.sqrt(num)
	cfrac = []
	frac = [1,1]
	denom = 0
	if x % 1 != 0:
		while frac[1] <= limit:
			denom = int(frac[1])
			cfrac.append(x//1)
			x = 1 / (x- x//1)
			frac = simp(chain_to_frac(cfrac))
			#vi skal bruge en ny "while" der tjekker hele vejen op til tallet..? Lyder langt
	print ("fra %s fik vi %s" % (num, denom))
	return denom

n = 100
sum = 0

for i in range(13,13 + 1):
	sum += best_frac_below(i, n)

print (sum)
	
stop = timeit.default_timer()
print (stop - start)