import unittest

"""
Almost Pi

Let fn(k) = ek/n - 1, for all non-negative integers k.
Remarkably, f200(6) + f200(75) + f200(89) + f200(226) = 3.141592644529… ≈ π.
In fact, it is the best approximation of π of the form fn(a) + fn(b) + fn(c) + fn(d) for n = 200.
Let g(n) = a2 + b2 + c2 + d 2 for a, b, c, d that minimize the error: | fn(a) + fn(b) + fn(c) + fn(d) - π|
(where |x| denotes the absolute value of x).
You are given g(200) = 62 + 752 + 892 + 2262 = 64658.
Find g(10000).
"""


class Test(unittest.TestCase):
    def test(self):
        pass
