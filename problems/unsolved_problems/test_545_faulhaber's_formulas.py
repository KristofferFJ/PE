import unittest

"""
Faulhaber's Formulas

The sum of the kth powers of the first n positive integers can be expressed as a polynomial of degree k+1 with rational coefficients, the Faulhaber's Formulas:
$1^k + 2^k + ... + n^k = \sum_{i=1}^n i^k = \sum_{i=1}^{k+1} a_{i} n^i = a_{1} n + a_{2} n^2 + ... + a_{k} n^k + a_{k+1} n^{k + 1}$,
where ai's are rational coefficients that can be written as reduced fractions pi/qi (if ai = 0, we shall consider qi = 1).
For example, $1^4 + 2^4 + ... + n^4 = -\frac 1 {30} n + \frac 1 3 n^3 + \frac 1 2 n^4 + \frac 1 5 n^5.$
Define D(k) as the value of q1 for the sum of kth powers (i.e. the denominator of the reduced fraction a1).
Define F(m) as the mth value of k ≥ 1 for which D(k) = 20010.
You are given D(4) = 30 (since a1 = -1/30), D(308) = 20010, F(1) = 308, F(10) = 96404.
Find F(105).
"""


class Test(unittest.TestCase):
    def test(self):
        pass
