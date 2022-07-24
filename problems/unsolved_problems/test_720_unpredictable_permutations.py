import unittest

"""
Unpredictable Permutations

Consider all permutations of $\{1, 2, \ldots N\}$, listed in lexicographic order.For example, for $N=4$, the list starts as follows:

Let us call a permutation $P$ unpredictable if there is no choice of three indices $i \lt j \lt k$ such that $P(i)$, $P(j)$ and $P(k)$ constitute an arithmetic progression. For example, $P=(3, 4, 2, 1)$ is not unpredictable because $P(1), P(3), P(4)$ is an arithmetic progression.


Let $S(N)$ be the position within the list of the first unpredictable permutation.


For example, given $N = 4$, the first unpredictable permutation is $(1, 3, 2, 4)$ so $S(4) = 3$.
You are also given that $S(8) = 2295$ and $S(32) \equiv 641839205 \pmod{1\,000\,000\,007}$.


Find $S(2^{25})$. Give your answer modulo $1\,000\,000\,007$.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
