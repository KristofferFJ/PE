import unittest

# Paper-strip Game
""" 
The following game is a classic example of Combinatorial Game Theory:
Two players start with a strip of $n$ white squares and they take alternate turns.
On each turn, a player picks two contiguous white squares and paints them black.
The first player who cannot make a move loses.
So, for $1 \le n \le 5$, there are 3 values of $n$ for which the first player can force a win.
Similarly, for $1 \le n \le 50$, there are 40 values of $n$ for which the first player can force a win.
For $1 \le n \le 1 000 000$, how many values of $n$ are there for which the first player can force a win?
""" 


class Test(unittest.TestCase):
    def test(self):
        pass
