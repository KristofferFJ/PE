#48 - SELF POWERS
#Hvad er summen af de 10 sidste cifre af summen 1**1 + 2**2 + ... + 1000**1000?

import timeit
start = timeit.default_timer()

def self_power_mod10(n):
	self_power = 1
	for i in range(n):
		self_power = (self_power*n)%(10**10) 
	return self_power
	
sum = 0
for i in range(1,1001):
	sum =(sum+ self_power_mod10(i)) % (10**10)

print (sum)
	
print (timeit.default_timer() - start)