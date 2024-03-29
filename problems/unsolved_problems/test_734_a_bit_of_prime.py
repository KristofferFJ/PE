import unittest

"""
A bit of prime


The logical-OR of two bits is 0 if both bits are 0, otherwise it is 1.
The bitwise-OR of two positive integers performs a logical OR operation on each pair of corresponding bits in the binary expansion of its inputs.


For example, the bitwise-OR of $10$ and $6$ is $14$ because $10 = 1010_2$, $6 = 0110_2$ and $14 = 1110_2$.


Let $T(n, k)$ be the number of $k$-tuples $(x_1, x_2,\cdots,x_k)$ such that


For example, $T(5, 2)=5$. The five 2-tuples are (2, 2), (2, 3), (3, 2), (3, 3) and (5, 5).


You are given $T(100, 3) = 3355$ and $T(1000, 10) \equiv 2071632 \pmod{1\,000\,000\,007}$


Find $T(10^6,999983)$. Give your answer modulo $1\,000\,000\,007$

"""


class Test(unittest.TestCase):
    def test(self):
        pass
