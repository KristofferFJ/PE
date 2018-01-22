#ALMINDELIGE FUNKTIONER

def factors(n):
	primes = []
	while n != 1:
		for i in range(2,n+1):
			if n % i == 0:
				n = n // i
				primes.append(i)
				break
	return primes

def primes(n):
	list = [True]*(n+1)
	list[0]=list[1]=False
	for i in range(2,int(n**.5)):
		ii = i*i
		while ii <= n:
			list[ii] = False
			ii += i
	return list
	
def fact(n):
	if n == 0:
		return 1
	elif n == 1:
		return n
	else:
		return n*fact(n-1)
		
def anagram(n,m):
	a,b = str(n), str(m)
	value = True
	for i in range(10):
		if a.count(str(i)) != b.count(str(i)):
			value = False
	return value
	
def gcd(x, y):
	while (y != 0):
		x, y = y, x % y
	return x