import unittest

# Cyclogenic Polynomials
"""
A monic polynomial is a single-variable polynomial in which the coefficient of highest degree is equal to 1.
Define $\mathcal{F}$ to be the set of all monic polynomials with integer coefficients (including the constant polynomial $p(x)=1$). A polynomial $p(x)\in\mathcal{F}$ is cyclogenic if there exists $q(x)\in\mathcal{F}$ and a positive integer $n$ such that $p(x)q(x)=x^n-1$. If $n$ is the smallest such positive integer then $p(x)$ is $n$-cyclogenic.
Define $P_n(x)$ to be the sum of all $n$-cyclogenic polynomials. For example, there exist ten 6-cyclogenic polynomials (which divide $x^6-1$ and no smaller $x^k-1$):
giving
Also define
It's given that
$Q_{10}(x)=x^{10}+3x^9+3x^8+7x^7+8x^6+14x^5+11x^4+18x^3+12x^2+23x$ and $Q_{10}(2) = 5598$.
Find $Q_{10^7}(2)$. Give your answer modulo $1\,000\,000\,007$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
