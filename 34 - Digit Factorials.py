#DIGIT FACTORIALS: Find de numre, hvis cifres fakultet er lige med tallet.
#Første metode gik galt: Den tog fakultet for en masse 0'er.. ups.
from Common import fact

"""
count = -2
for i in range(3):
	for j in range(10):
		print ("j er nu "+str(j))
		for k in range(10):
			for l in range(10):
				for m in range(10):
					for n in range(10):
						for o in range(10):
							if fact(i)+fact(j)+fact(k)+fact(l)+fact(m)+fact(n)+fact(o) == 1*o + 10*n + 10**2*m + 10**3*l+10**4*k+10**5*j+10**6*i:
								count +=1
							"""
							
def digit_factorial(n):
	j = str(n)
	fact_sum = 0
	for k in range(len(j)):
		fact_sum += fact(int(j[k]))
	if fact_sum == n:
		print ("Det dur for n ="+str(n))
		return True
		
#for i in range(1,200000):
	#digit_factorial(i)
	
#Lækker løsning med list comprehension jeg så:
factorials = [1,1,2,6,24,120,720,5040,40320,362880]
s = 0
for i in range(3,100000):
	if i==sum(factorials[int(j)] for j in str(i)):
		s += i
print (s)