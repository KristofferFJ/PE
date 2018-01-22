import timeit

start = timeit.default_timer()

num = 10**6

#Peter slår 9 4'ere og Svend(?) slår 6 6'ere. Hvad er sandsynligheden for at Peter vinder?

tetra = [0]*(37)
hexa = [0]*(37)

for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			for l in range(1,5):
				for m in range(1,5):
					for n in range(1,5):
						for o in range(1,5):
							for p in range(1,5):
								for q in range(1,5):
									tetra[i+j+k+l+m+n+o+p+q] += 1
									
for i in range(1,7):
	for j in range(1,7):
		for k in range(1,7):
			for l in range(1,7):
				for m in range(1,7):
					for n in range(1,7):
						hexa[i+j+k+l+m+n] += 1			
			
pow4 = 4**9
pow6 = 6**6
for i in range(1,37):
	tetra[i] /= pow4
	hexa[i] /= pow6

pWin = 0
for i in range(9,37):
	j = 6
	while i > j:
		pWin += tetra[i]*hexa[j]
		j += 1

print (pWin)		

print (timeit.default_timer() - start)