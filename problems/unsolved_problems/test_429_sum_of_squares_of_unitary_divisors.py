import unittest

"""
Sum of squares of unitary divisors


A unitary divisor d of a number n is a divisor of n that has the property gcd(d, n/d) = 1.
The unitary divisors of 4! = 24 are 1, 3, 8 and 24.
The sum of their squares is 12 + 32 + 82 + 242 = 650.


Let S(n) represent the sum of the squares of the unitary divisors of n. Thus S(4!)=650.


Find S(100 000 000!) modulo 1 000 000 009.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
