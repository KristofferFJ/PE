# PERMUTED MULTIPLES
# Find det mindste tal så x, 2x, 3x, 4x, 5x og 6x alle har samme cifre.

from common import anagram
import timeit

start = timeit.default_timer()

found = False
i = 1
while not found:
    if anagram(i, 2*i):
        if anagram(i, 3*i):
            if anagram(i, 4*i):
                if anagram(i, 5*i):
                    if anagram(i, 6*i):
                        found = True
                        print(i)
    i += 1

print(timeit.default_timer() - start)
