import unittest

"""
Constraining the least greatest and the greatest least

A list of size n is a sequence of n natural numbers. Examples are (2,4,6), (2,6,4), (10,6,15,6), and (11).


The greatest common divisor, or gcd, of a list is the largest natural number that divides all entries of the list. Examples: gcd(2,6,4) = 2, gcd(10,6,15,6) = 1 and gcd(11) = 11.


The least common multiple, or lcm, of a list is the smallest natural number divisible by each entry of the list. Examples: lcm(2,6,4) = 12, lcm(10,6,15,6) = 30 and lcm(11) = 11.


Let f(G, L, N) be the number of lists of size N with gcd ≥ G and lcm ≤ L. For example:


f(10, 100, 1) = 91.
f(10, 100, 2) = 327.
f(10, 100, 3) = 1135.
f(10, 100, 1000) mod 1014 = 3286053.


Find f(106, 1012, 1018) mod 1014.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
