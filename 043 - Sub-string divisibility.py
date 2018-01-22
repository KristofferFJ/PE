#43 Sub-string divisibility

from itertools import permutations

primes = [2,3,5,7,11,13,17]

candidates = permutations([i for i in range(10)])
succes = []

for perm in candidates:
	possible = True
	i = 1
	while possible and i < 8:
		if int(str(perm[i])+str(perm[i+1])+str(perm[i+2])) % primes[i-1] != 0:
			possible = False
		else:
			i += 1
	if possible:
		number = (10**9 * perm[0] + 10**8 * perm[1] + 10**7 * perm[2]
				+ 10**6 * perm[3] + 10**5 * perm[4] + 10**4 * perm[5]
				+ 10**3 * perm[6] + 10**2 * perm[7] + 10**1 * perm[8]
				+ 10**0 * perm[9])
		succes.append(number)