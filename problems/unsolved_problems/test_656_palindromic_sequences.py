import unittest

"""
Palindromic sequences


Given an irrational number $\alpha$, let $S_\alpha(n)$ be the sequence $S_\alpha(n)=\lfloor {\alpha \cdot n} \rfloor - \lfloor {\alpha \cdot (n-1)} \rfloor$ for $n \ge 1$. 
($\lfloor ... \rfloor$ is the floor-function.)


It can be proven that for any irrational $\alpha$ there exist infinitely many values of $n$ such that the subsequence $ \{S_\alpha(1),S_\alpha(2)...S_\alpha(n) \} $ is palindromic.

The first 20 values of $n$  that give a palindromic subsequence for $\alpha = \sqrt{31}$ are:
1, 3, 5, 7, 44, 81, 118, 273, 3158, 9201, 15244, 21287, 133765, 246243, 358721, 829920, 9600319, 27971037, 46341755, 64712473.

Let $H_g(\alpha)$ be the sum of the first $g$ values of $n$  for which the corresponding subsequence is palindromic.
So $H_{20}(\sqrt{31})=150243655$.


Let $T=\{2,3,5,6,7,8,10,...,1000\}$ be the set of positive integers, not exceeding 1000, excluding perfect squares.
Calculate the sum of $H_{100}(\sqrt \beta)$ for  $\beta \in T$. Give the last 15 digits of your answer.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
