import unittest

# One more one
"""
Consider the following process that can be applied recursively to any positive integer $n$:
Define $g(n)$ to be the number of 1's that must be added before the process ends. For example:
Eight 1's are added so $g(125) = 8$. Similarly $g(1000) = 9$ and $g(10000) = 21$.
Define $S(N) = \sum_{n=1}^{N} g(n)$ and $H(K) = S\left(\frac{7^K-1}{11}\right)$. You are given $H(10) = 690409338$.
Find $H(10^9)$ modulo $1\,117\,117\,717$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
