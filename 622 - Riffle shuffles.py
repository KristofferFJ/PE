# 622 Riffle shuffles
# A riffle shuffle is executed as follows:
# a deck of cards is split into two equal halves,
# with the top half taken in the left hand and the bottom half taken in the right hand.
# Next, the cards are interleaved exactly, with the top card in the right half inserted just after
# the top card in the left half, the 2nd card in the right half just after the 2nd card in the left half, etc.
# (Note that this process preserves the location of the top and bottom card of the deck)
# Let s(n) be the minimum number of consecutive riffle shuffles needed to restore a deck
# of size n to its original configuration, where n is a positive even number.
# Amazingly, a standard deck of 52 cards will first return to its original configuration after only 8 perfect shuffles,
# so s(52)=8. It can be verified that a deck of 86 cards will also return to its original
# configuration after exactly 8 shuffles, and the sum of all values of n that satisfy s(n)=8 is 412.
# Find the sum of all values of n that satisfy s(n)=60.

import time
import Library.common as cm


def main():
    power_of_2 = 60
    bignum = 2**power_of_2-1
    factors = cm.factors(bignum)
    lower_number_of_shuffles = [2**i - 1 for i in range(1, power_of_2)]
    primitive_divisors = []
    for divisor in factors:
        primitive_divisor = True
        for number in lower_number_of_shuffles:
            if number % divisor == 0:
                primitive_divisor = False
        if primitive_divisor:
            primitive_divisors.append(divisor + 1)

    print("Summen af alle tal, der kræver 60 riffle shuffles for at vende tilbage til normal er %s" % sum(primitive_divisors))


if __name__ == '__main__':
    start = time.time()
    main()
    print("Løsningen tog %s sekunder" % (time.time() - start))
