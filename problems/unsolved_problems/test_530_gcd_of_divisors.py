import unittest

"""
GCD of Divisors

Every divisor d of a number n has a complementary divisor n/d.
Let f(n) be the sum of the greatest common divisor of d and n/d over all positive divisors d of n, that is
$f(n)=\displaystyle\sum\limits_{d|n}\, \text{gcd}(d,\frac n d)$.
Let F be the summatory function of f, that is
$F(k)=\displaystyle\sum\limits_{n=1}^k \, f(n)$.
You are given that F(10)=32 and F(1000)=12776.
Find F(1015).
"""


class Test(unittest.TestCase):
    def test(self):
        pass
