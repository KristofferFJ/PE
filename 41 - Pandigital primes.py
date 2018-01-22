#PROBLEM 41 - PANDIGITAL PRIMES: 3 går op i summen af tallene fra 1 - 8 og 1 - 9 så vi skal kun tjekke primtal med tallene fra 1-7.

num = 10**7
primes = [True] * num
primes[0]=primes[1]=False

for i in range(int(num**.5)):
	if primes[i]:
		ii = i*i
		while ii < num:
			primes[ii] = False
			ii += i

max = 0

def pan_check(n):
	pandigit = True
	for i in range(1,len(str(n))+1):
		if str(i) not in str(n):
			pandigit = False
	return pandigit
		
for j in range(len(primes)):
	if primes[j]:
		if pan_check(j):
			max = j
			
print (max)