# 48 - SELF POWERS
# Hvad er smen af de 10 sidste cifre af smen 1**1 + 2**2 + ... + 1000**1000?

import timeit
start = timeit.default_timer()


def self_power_mod10(n):
    self_power = 1
    for i in range(n):
        self_power = (self_power*n)%(10**10)
    return self_power


s = 0
for i in range(1,1001):
    s =(s+ self_power_mod10(i)) % (10**10)

print(s)

print(timeit.default_timer() - start)