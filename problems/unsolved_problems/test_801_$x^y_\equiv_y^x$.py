import unittest

# $x^y \equiv y^x$
# 
# The positive integral solutions of the equation $x^y=y^x$ are $(2,4)$, $(4,2)$ and $(k,k)$ for all $k > 0$.
# For a given positive integer $n$, let $f(n)$ be the number of integral values $0 < x,y \leq n^2-n$ such that
$$x^y\equiv y^x \pmod n$$
For example, $f(5)=104$ and $f(97)=1614336$.
# Let $S(M,N)=\sum f(p)$ where the sum is taken over all primes $p$ satisfying $M\le p\le N$.
# You are given $S(1,10^2)=7381000$ and $S(1,10^5) \equiv 701331986 \pmod{993353399}$.
# Find $S(10^{16}, 10^{16}+10^6)$. Give your answer modulo $993353399$.


class Test(unittest.TestCase):
	pass
