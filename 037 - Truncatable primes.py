#TRUNCATABLE PRIMES: Primtal, der stadig er primtal når man fjerner
#cifre fra højre og venstre. 2,3 og 7 tæller ikke.

from common import primes
num = 10**6
list = primes(num)
plist = [i for i in range(10,len(list)) if list[i]]

count = 0
s = 0
for p in plist:
	prime = True
	a,b = p,p
	while a > 10:
		pot = len(str(a))-1
		a = a%(10**pot)
		if list[a] == False:
			prime = False
			break
	while b > 10:
		b = b//10
		if list[b] == False:
			prime = False
			break
	if prime:
		count += 1
		s += p
		print (p)

print (count)
print (s)