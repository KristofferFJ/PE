import unittest

"""
Coprime Nim

Coprime Nim is just like ordinary normal play Nim, but the players may only remove a number of stones from a pile  that is coprime with the current size of the pile. Two players remove stones in turn. The player who removes the last stone wins.
Let L(n, k) be the number of losing starting positions for the first player, assuming perfect play, when the game is played with k piles, each having between 1 and n - 1 stones inclusively.
For example, L(5, 2) = 6 since the losing initial positions are (1, 1), (2, 2), (2, 4), (3, 3), (4, 2) and (4, 4).
You are also given L(10, 5) = 9964, L(10, 10) = 472400303, L(103, 103) mod 1 000 000 007 = 954021836.
Find L(107, 107) mod 1 000 000 007
"""


class Test(unittest.TestCase):
    def test(self):
        pass
