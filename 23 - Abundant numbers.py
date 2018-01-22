#ABUNDANT NUMBERS

import timeit

start = timeit.default_timer()

num = 28123 
"""
def divisors(n):
	divisors = [1]
	for i in range(2,int(n**.5)+1):
		if n % i == 0:
			divisors.append(i)
			if n // i != i:
				divisors.append(n // i)
	return divisors

def divisor_sum(list):
	sum = 0
	for i in range(len(list)):
		sum += list[i]
	return sum

def abundants(n):
	abundants = []
	for i in range(1, n):
		if divisor_sum(divisors(i)) > i:
			abundants.append(i)
	return abundants

list = abundants(num)
not_sum = [True] * (num+1)

for i in range(len(list)):
	j = i
	while list[i] + list[j] <= num and j < len(list):
		not_sum[list[i]+list[j]] = False
		j += 1
	
sum = 0
for i in range(len(not_sum)):
	if not_sum[i]:
		sum += i

print (sum)
"""
#SET LØSNING
def div_sum(n):
	div = set([1])
	for i in range(2,int(n**.5)+1):
		if n % i == 0:
			div.add(i)
			div.add(n / i)
	return sum(div)

ab = set(i for i in range(1,num+1) if div_sum(i) > i)
ss = set(i + j for i in ab for j in ab if i + j <= num)
zs = set(range(1,num+1))

print(sum(zs-ss))
	
print (timeit.default_timer() - start)