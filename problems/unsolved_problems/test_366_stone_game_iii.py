import unittest

"""
Stone Game III


Two players, Anton and Bernhard, are playing the following game.
There is one pile of n stones.
The first player may remove any positive number of stones, but not the whole pile.
Thereafter, each player may remove at most twice the number of stones his opponent took on the previous move.
The player who removes the last stone wins.


E.g. n=5
If the first player takes anything more than one stone the next player will be able to take all remaining stones.
If the first player takes one stone, leaving four, his opponent will take also one stone, leaving three stones.
The first player cannot take all three because he may take at most 2x1=2 stones. So let's say he takes also one stone, leaving 2. The second player can take the two remaining stones and wins.
So 5 is a losing position for the first player.
For some winning positions there is more than one possible move for the first player.
E.g. when n=17 the first player can remove one or four stones.


Let M(n) be the maximum number of stones the first player can take from a winning position at his first turn and M(n)=0 for any other position.


∑ M(n) for n≤100 is 728.


Find  ∑ M(n) for n≤1018.
Give your answer modulo 108.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
