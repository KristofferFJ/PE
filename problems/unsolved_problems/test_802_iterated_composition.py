import unittest

"""
Iterated Composition

Let $\Bbb R^2$ be the set of pairs of real numbers $(x, y)$. Let $\pi = 3.14159\cdots\ $.
Consider the function $f$ from $\Bbb R^2$ to $\Bbb R^2$ defined by $f(x, y) = (x^2 - x - y^2, 2xy - y + \pi)$, and its $n$-th iterated composition $f^{(n)}(x, y) = f(f(\cdots f(x, y)\cdots))$. For example $f^{(3)}(x, y) = f(f(f(x, y)))$. A pair $(x, y)$ is said to have period $n$ if $n$ is the smallest positive integer such that $f^{(n)}(x, y) = (x, y)$.
Let $P(n)$ denote the sum of $x$-coordinates of all points having period not exceeding $n$.
Interestingly, $P(n)$ is always an integer. For example, $P(1) = 2$, $P(2) = 2$, $P(3) = 4$.
Find $P(10^7)$ and give your answer modulo $1\,020\,340\,567$.
"""

class Test(unittest.TestCase):
    def test(self):
        pass
