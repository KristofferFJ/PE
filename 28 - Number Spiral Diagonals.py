#Find summen af diagonalerne i en talspiral.

sum = 1
for i in range(1,501):
	sum += 2*(2*(i*2+1)**2 - 6*i)
	
print (sum)