import unittest

# Nontransitive sets of dice
""" 

Consider the following set of dice with nonstandard pips:


Die A: 1 4 4 4 4 4
Die B: 2 2 2 5 5 5
Die C: 3 3 3 3 3 6

A game is played by two players picking a die in turn and rolling it. The player who rolls the highest value wins.


If the first player picks die A and the second player picks die B we get
P(second player wins) = 7/12 > 1/2

If the first player picks die B and the second player picks die C we get
P(second player wins) = 7/12 > 1/2

If the first player picks die C and the second player picks die A we get
P(second player wins) = 25/36 > 1/2

So whatever die the first player picks, the second player can pick another die and have a larger than 50% chance of winning.
A set of dice having this property is called a nontransitive set of dice.


We wish to investigate how many sets of nontransitive dice exist. We will assume the following conditions:

For N = 7 we find there are 9780 such sets.
How many are there for N = 30 ?

""" 


class Test(unittest.TestCase):
    def test(self):
        pass
