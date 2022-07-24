import unittest

"""
Blood tests


Each one of the 25 sheep in a flock must be tested for a rare virus, known to affect 2% of the sheep population.
An accurate and extremely sensitive PCR test exists for blood samples, producing a clear positive / negative result, but it is very time-consuming and expensive.


Because of the high cost, the vet-in-charge suggests that instead of performing 25 separate tests, the following procedure can be used instead:
The sheep are split into 5 groups of 5 sheep in each group. 
For each group, the 5 samples are mixed together and a single test is performed. Then,


Since the probability of infection for any specific animal is only 0.02, the first test (on the pooled samples) for each group will be:


Thus, the expected number of tests for each group is 1 + 0.0960792032 × 5 = 1.480396016.
Consequently, all 5 groups can be screened using an average of only 1.480396016 × 5 = 7.40198008 tests, which represents a huge saving of more than 70% !


Although the scheme we have just described seems to be very efficient, it can still be improved considerably (always assuming that the test is sufficiently sensitive and that there are no adverse effects caused by mixing different samples). E.g.:


To simplify the very wide range of possibilities, there is one restriction we place when devising the most cost-efficient testing scheme: whenever we start with a mixed sample, all the sheep contributing to that sample must be fully screened (i.e. a verdict of infected / virus-free must be reached for all of them) before we start examining any other animals.


Using the optimal strategy, let T(s,p) represent the average number of tests needed to screen a flock of s sheep for a virus having probability p to be present in any individual.
Thus, rounded to six decimal places, T(25, 0.02) = 4.155452 and T(25, 0.10) = 12.702124.


Find ∑ T(10000, p) for p=0.01, 0.02, 0.03, ... 0.50.
Give your answer rounded to six decimal places.

"""

class Test(unittest.TestCase):
    def test(self):
        pass
