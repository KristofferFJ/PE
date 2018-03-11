#569 Prime mountain range
"""
A mountain range consists of a line of mountains with slopes of exactly 45°,
and heights governed by the prime numbers, pn. The up-slope of the kth mountain is of height p2k−1,
and the downslope is p2k. The first few foot-hills of this range are illustrated below.

p569-prime-mountain-range.gif

Tenzing sets out to climb each one in turn, starting from the lowest.
At the top of each peak, he looks back and counts how many of the previous peaks he can see.
In the example above, the eye-line from the third mountain is drawn in red, showing that he can only
see the peak of the second mountain from this viewpoint. Similarly, from the 9th mountain, he can see three peaks, those of the 5th, 7th and 8th mountain.

Let P(k) be the number of peaks that are visible looking back from the kth mountain. Hence P(3)=1 and P(9)=3."""

from sympy import sieve
import time
import numpy as np

# By 2.5 * 10**4 : 142491
# By 2.5 * 10**3	: 10783
# By 100 		: 227

start = time.time()

bignum = int(2.5 * 10**3)


heights = [0,2]
for i in range(2, bignum + 1):
    heights.append(heights[i-1] - sieve[2*(i-1)] + sieve[2*i - 1])

lengths = [0,2]
for i in range(2, bignum + 1):
    lengths.append(lengths[i-1] + sieve[2*(i-1)] + sieve[2*i - 1])

def slope_to(n):
    return (heights[n] - heights[n-1]) / (lengths[n] - lengths[n-1])

def main(n):
    start = time.time()
    n = int(n)
    peaks = 0
    records = [0,10**12]
    heights = [0,2]
    lengths = [0,2]
    for i in range(2, n + 1):
        height = heights[i-1] - sieve[2*(i-1)] + sieve[2*i - 1]
        heights.append(height)
        length = lengths[i-1] + sieve[2*(i-1)] + sieve[2*i - 1]
        lengths.append(length)
        slope = (height - heights[i-1]) / (length - lengths[i-1])
        if slope < records[i-1]:
            records.append(slope)
            peaks += 1
        else:
            records.append(records[i-1])
        j = i
        temp_rec = slope
        while slope > records[j - 1] and j > 1:
            if slope <= temp_rec:
                peaks += 1
                temp_rec = slope
            slope = (height - heights[j - 2]) / (length - lengths[j - 2])
            j -= 1
        print("Efter %s er vi oppe på %s" % (i, peaks))
    return (peaks + 7, time.time() - start)

def peak(n):
    peaks = 0
    slope = 10**12
    for i in range(n-1, 0, -1):
        slope_to_i = (heights[n] - heights[i]) / (lengths[n] - lengths[i])
        if slope_to_i < slope:
            print("Fik en fra " + str(i))
            peaks += 1
            slope = slope_to_i
    return peaks

print (time.time() - start)
#New peak-counter which only check the lowest

#print (s(peak(i) for i in range(2,bignum + 1)), time.time() - start)