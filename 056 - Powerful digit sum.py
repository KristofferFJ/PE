#POWERFUL DIGIT s
#Hvilket tal a^b med a,b < 100 har højeste tværs?

maximum = 0

for a in range(1,100):
	for b in range(1,100):
		s = s(int(i) for i in str(a**b))
		if s > maximum:
			maximum = s
			
print (maximum)

#Eller en one-liner:

print (max(s(int(i) for i in str(a**b)) for a in range(1,100) for b in range(1,100)))
