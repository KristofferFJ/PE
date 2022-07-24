import unittest

"""
Euler's Number

For example,
$a(0) = \dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \cdots = e - 1$
$a(1) = \dfrac{e - 1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \cdots = 2e - 3$
$a(2) = \dfrac{2e - 3}{1!} + \dfrac{e - 1}{2!} + \dfrac{1}{3!} + \cdots = \dfrac{7}{2}e - 6$
with $e = 2.7182818...$ being Euler's constant.
It can be shown that $a(n)$ is of the form $\dfrac{A(n)e + B(n)}{n!}$ for integers $A(n)$ and $B(n)$.
For example, $a(10) = \dfrac{328161643e - 652694486}{10!}$.
Find $A(10^9) + B(10^9)$ and give your answer mod 77 777 777.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
