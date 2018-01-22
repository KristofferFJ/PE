#COMBINATORIC SELECTIONS
#Hvor mange binomialkoefficienter med 1<= n <= 100 er større end
#en million?
import timeit
start = timeit.default_timer()

def factorial(n):
	if n==0:
		return 1
	elif n==1:
		return n
	else:
		return n*factorial(n-1)

count = 0
for i in range(1,101):
	j = 0
	while j < i/2:
		fact = factorial(i)/(factorial(i-j)*factorial(j))
		if fact >= 10**6:
			count += 2
		j += 1
for i in range(1,51):
	fact = factorial(2*i)/(factorial(i)**2)
	if fact >= 10**6:
		count += 1
		
print (count)
print (timeit.default_timer() - start)