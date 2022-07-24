import unittest

"""
Number Sequence Game

The number sequence game starts with a sequence S of N numbers written on a line.
Two players alternate turns. The players on their respective turns must select and remove either the first or the last number remaining in the sequence.
A player's own score is (determined by) the sum of all the numbers that player has taken. Each player attempts to maximize their own sum.
Player 1 score is 1 + 10 = 11.
Let F(N) be the score of player 1 if both players follow the optimal strategy for the sequence S = {s1, s2, ..., sN} defined as:
The sequence begins with S = {0, 45, 2070, 4284945, 753524550, 478107844, 894218625, ...}.
You are given F(2) = 45, F(4) = 4284990, F(100) = 26365463243, F(104) = 2495838522951.
Find F(108).
"""


class Test(unittest.TestCase):
    def test(self):
        pass
