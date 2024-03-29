import unittest

"""
Proportionate Nim

Two players play a game with two piles of stones, alternating turns.
On each turn, the corresponding player chooses a positive integer $n$ and does one of the following:
The player who removes the last stone wins.
We denote by $(n,m)$ the position in which the piles have $n$ and $m$ stones remaining. Note that $(n,m)$ is considered to be the same position as $(m,n)$.
Then, for example, if the position is $(2,6)$, the next player may reach the following positions:
$(0,2)$, $(0,4)$, $(0,5)$, $(0,6)$, $(1,2)$, $(1,4)$, $(1,5)$, $(1,6)$, $(2,2)$, $(2,3)$, $(2,4)$, $(2,5)$
A position is a losing position if the player to move next cannot force a win. For example, $(1,3)$, $(2,6)$, $(4,5)$ are the first few losing positions.
Let $f(M)$ be the sum of $n+m$ for all losing positions $(n,m)$ with $n\le m$ and $n+m \le M$. For example, $f(10) = 21$, by considering the losing positions $(1,3)$, $(2,6)$, $(4,5)$.
You are given that $f(100) = 1164$ and $f(1000) = 117002$.
Find $f(10^7)$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
