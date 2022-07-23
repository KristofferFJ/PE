import unittest

# Sextuplet Norms
""" 
Let $f(n)$ be the number of $6$-tuples $(x_1,x_2,x_3,x_4,x_5,x_6)$ such that:
Let $\displaystyle G(n)=\displaystyle\sum_{k=1}^n \frac{f(k)}{k^2\varphi(k)}$
where $\varphi(n)$ is Euler's totient function.
For example, $G(10)=3053$ and $G(10^5) \equiv 157612967 \pmod{1\,000\,000\,007}$.
Find $G(10^{12})\bmod 1\,000\,000\,007$.
""" 


class Test(unittest.TestCase):
    def test(self):
        pass
