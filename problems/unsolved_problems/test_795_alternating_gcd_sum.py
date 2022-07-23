import unittest

# Alternating GCD Sum
"""

For a positive integer $n$, the function $g(n)$ is defined as


For example, $g(4) = -\gcd \left(4,1^2\right) + \gcd \left(4,2^2\right) - \gcd \left(4,3^2\right) + \gcd \left(4,4^2\right) = -1+4-1+4=6$.
You are also given $g(1234)=1233$.


Let $\displaystyle G(N) = \sum_{n=1}^N g(n)$. You are given $G(1234) = 2194708$.


Find $G(12345678)$.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
