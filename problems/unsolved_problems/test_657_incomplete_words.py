import unittest

"""
Incomplete words

In the context of formal languages, any finite sequence of letters of a given alphabet $\Sigma$ is called a word over $\Sigma$. We call a word incomplete if it does not contain every letter of $\Sigma$.

For example, using the alphabet $\Sigma=\{ a, b, c\}$, '$ab$', '$abab$' and '$\,$' (the empty word) are incomplete words over $\Sigma$, while '$abac$' is a complete word over $\Sigma$.

Given an alphabet $\Sigma$ of $\alpha$ letters, we define $I(\alpha,n)$ to be the number of incomplete words over $\Sigma$ with a length not exceeding $n$. 
For example, $I(3,0)=1$, $I(3,2)=13$ and $I(3,4)=79$.

Find $I(10^7,10^{12})$. Give your answer modulo $1\,000\,000\,007$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
