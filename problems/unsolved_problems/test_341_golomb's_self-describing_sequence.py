import unittest

# Golomb's self-describing sequence
"""
The Golomb's self-describing sequence $(G(n))$ is the only nondecreasing sequence of natural numbers such that $n$ appears exactly $G(n)$ times in the sequence. The values of $G(n)$ for the first few $n$ are

You are given that $G(10^3) = 86$, $G(10^6) = 6137$.
You are also given that $\sum G(n^3) = 153506976$ for $1 \le n \lt 10^3$.
Find $\sum G(n^3)$ for $1 \le n \lt 10^6$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
