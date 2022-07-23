import unittest

# Minimum of subsequences
"""
Let $S_n$ be an integer sequence produced with the following pseudo-random number generator:

Let $A(i, j)$ be the minimum of the numbers $S_i, S_{i+1}, \ldots, S_j$ for $i\le j$.
Let $M(N) = \sum A(i, j)$ for $1 \le i \le j \le N$.
We can verify that $M(10) = 432256955$ and $M(10\,000) = 3264567774119$.

Find $M(2\,000\,000\,000)$.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
