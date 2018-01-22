import itertools
import timeit

start = timeit.default_timer()

perm = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))[1000000-1]

print (perm)

#LAV ALTERNATIV METODE

print (timeit.default_timer() - start)