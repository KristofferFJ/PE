import unittest

"""
Verifying Primes

Let $q$ be a prime and $A \ge B >0$ be two integers with the following properties:

It can be shown that, given these conditions, any sum $A+B<q^2$ and any difference $1<A-B<q^2$ has to be a prime number. Thus you can verify that a number $p$ is prime by showing that either $p=A+B<q^2$ or $p=A-B<q^2$ for some $A,B,q$ fulfilling the conditions listed above.
Let $V(p)$ be the smallest possible value of $A$ in any sum $p=A+B$ and any difference $p=A-B$, that verifies $p$ being prime. Examples:
$V(2)=1$, since $2=1+1< 2^2$. 
$V(37)=22$, since $37=22+15=2 \cdot 11+3 \cdot 5< 7^2$ is the associated sum with the smallest possible $A$.
$V(151)=165$ since $151=165-14=3 \cdot 5 \cdot 11 - 2 \cdot 7<13^2$ is the associated difference with the smallest possible $A$. 

Let $S(n)$ be the sum of $V(p)$ for all primes $p<n$. For example, $S(10)=10$ and $S(200)=7177$.

Find $S(3800)$.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
