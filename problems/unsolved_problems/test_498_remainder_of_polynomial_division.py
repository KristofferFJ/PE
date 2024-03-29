import unittest

"""
Remainder of polynomial division

For positive integers n and m, we define two polynomials Fn(x) = xn and Gm(x) = (x-1)m.
We also define a polynomial Rn,m(x) as the remainder of the division of Fn(x) by Gm(x).
For example, R6,3(x) = 15x2 - 24x + 10.
Let C(n, m, d) be the absolute value of the coefficient of the d-th degree term of Rn,m(x).
We can verify that C(6, 3, 1) = 24 and C(100, 10, 4) = 227197811615775.
Find C(1013, 1012, 104) mod 999999937.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
