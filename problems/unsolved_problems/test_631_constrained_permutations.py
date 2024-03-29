import unittest

"""
Constrained Permutations

Let $(p_1 p_2 \ldots p_k)$ denote the permutation of the set ${1, ..., k}$ that maps $p_i\mapsto i$. Define the length of the permutation to be $k$; note that the empty permutation $()$ has length zero.
Define an occurrence of a permutation $p=(p_1 p_2 \ldots p_k)$ in a permutation $P=(P_1 P_2 \ldots P_n)$ to be a sequence $1\leq t_1 < t_2 < \cdots < t_k \leq n$ such that $p_i < p_j$ if and only if $P_{t_i} < P_{t_j}$ for all $i,j \in \{1, ..., k\}$.
For example, $(1243)$ occurs twice in the permutation $(314625)$: once as the 1st, 3rd, 4th and 6th elements $(3\,\,46\,\,5)$, and once as the 2nd, 3rd, 4th and 6th elements $(\,\,146\,\,5)$.
Let $f(n, m)$ be the number of permutations $P$ of length at most $n$ such that there is no occurrence of the permutation $1243$ in $P$ and there are at most $m$ occurrences of the permutation $21$ in $P$.
For example, $f(2,0) = 3$, with the permutations $()$, $(1)$, $(1,2)$ but not $(2,1)$.
You are also given that $f(4, 5) = 32$ and $f(10, 25) = 294\,400$.
Find $f(10^{18}, 40)$ modulo $1\,000\,000\,007$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
