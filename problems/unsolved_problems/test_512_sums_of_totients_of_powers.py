import unittest

"""
Sums of totients of powers

Let $\varphi(n)$ be Euler's totient function.

Let $f(n)=(\sum_{i=1}^{n}\varphi(n^i)) \text{ mod } (n+1)$.

Let $g(n)=\sum_{i=1}^{n} f(i)$.

$g(100)=2007$.


Find $g(5 \times 10^8)$.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
