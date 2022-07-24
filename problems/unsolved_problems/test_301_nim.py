import unittest

"""
Nim

Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.
We'll consider the three-heap normal-play version of Nim, which works as follows:
If $(n_1,n_2,n_3)$ indicates a Nim position consisting of heaps of size $n_1$, $n_2$, and $n_3$, then there is a simple function, which you may look up or attempt to deduce for yourself, $X(n_1,n_2,n_3)$ that returns:
For example $X(1,2,3) = 0$ because, no matter what the current player does, the opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by the opponent until no stones remain; so the current player loses. To illustrate:
For how many positive integers $n \le 2^{30}$ does $X(n,2n,3n) = 0$ ?
"""


class Test(unittest.TestCase):
    def test(self):
        pass
