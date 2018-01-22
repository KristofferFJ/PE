#598 - Split Divisibilities
#Hvor mange divisorpar af 100! har ens antal divisorer?

prime_bool = [True for i in range(100+1)]
prime_bool[0] = prime_bool[1] = False

for i in range(2,10):
	j = i*i
	while j < 101:
		prime_bool[j] = False
		j += i
		
primes = []
for i in range(len(prime_bool)):
	if prime_bool[i]:
		primes.append(i)
		
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
	
prime_factors_100 = []
for i in range(2,101):
	for prime in prime_factors(i):
		prime_factors_100.append(prime)
		
numbers_of_divs = []
for prime in primes:
	numbers_of_divs.append(prime_factors_100.count(prime))
	
prod = 1
for div in numbers_of_divs:
	prod *= (div+1)