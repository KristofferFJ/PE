#PROBLEM 500: Find det mindste tal, der har 2**500500 divisorer. Svar module 500500507
#Hver primdivisor skal være repræsenteret 2**n - 1 gange for et eller andet n.
#Hver gang vi tilføjer et nyt primtal, skal vi tjekke om en af de tidligere kan
#tilføjes i større potens i stedet.
#Eks.: 2 er det mindste med 2 divisorer: 2 og 1. For at finde det mindste med 4 divisorer
#tjekker vi om 2**2 (så vi har 2**3 = 8) eller 3 (næste primtal) er størst. Det er 3
#så det mindste med 4 divisorer er 2*3.

num = 10**7
primes = [True]*(num+1)
primes[0]=primes[1]=False
for i in range(2,int(num**.5)):
	ii = i*i
	while ii<=num:
		primes[ii]=False
		ii += i
list_of_primes = []
for i in range(len(primes)):
	if primes[i]:
		list_of_primes.append(i)
	
div = 1
limit = 500500
list_of_divisors = [2]
j=1
min_index = 0
while div < limit:
	print ("Div er nu "+str(div))
	min = list_of_divisors[min_index] * list_of_primes[min_index]
	#print ("Minimum er nu %s" % min)
	p = list_of_primes[j]
	#print ("Og vi er kommet til %s" % p)
	if p < min:
		list_of_divisors.append(p)
		j += 1
	else:
		temp_index = 0
		list_of_divisors[min_index] = list_of_divisors[min_index]**2 * list_of_primes[min_index]
		temp_min = list_of_divisors[0] * list_of_primes[0]
		#print ("Temp_min er %s" % temp_min)
		for k in range(1,len(list_of_divisors)):
			if list_of_divisors[k] * list_of_primes[k] < temp_min:
				temp_min = list_of_divisors[k] * list_of_primes[k]
				temp_index = k
		#print ("Og vi tilføjer %s" % list_of_divisors[min_index])
		min_index = temp_index
	div += 1

#print (list_of_divisors)

prod = 1
for i in range(len(list_of_divisors)):
	prod = (prod*list_of_divisors[i])%500500507

print (prod)