#DISTINCT POWERS: Find hvor mange forskellige tal der af typen a**b hvor a og b ligger mellem 2 og 100.

pow = set()

for i in range(2,101):
	for j in range(2,101):
		pow.add(i**j)
		
print (len(pow))