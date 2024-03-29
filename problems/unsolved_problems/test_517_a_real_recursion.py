import unittest

"""
A real recursion


For every real number $a \gt 1$ is given the sequence $g_a$ by:
$g_{a}(x)=1$ for $x \lt a$
$g_{a}(x)=g_{a}(x-1)+g_a(x-a)$ for $x \ge a$

$G(n)=g_{\sqrt {n}}(n)$
$G(90)=7564511$.

Find $\sum G(p)$ for $p$ prime and $10000000 \lt p \lt 10010000$
Give your answer modulo 1000000007.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
