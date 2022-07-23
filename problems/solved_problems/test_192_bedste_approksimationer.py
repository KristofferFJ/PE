import timeit
import math

start = timeit.default_timer()


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def simp(l):
    x = int(l[0])
    y = int(l[1])
    x //= gcd(x, y)
    y //= gcd(x, y)
    return [x, y]


def chain_to_dec(l):
        x = l[len(l)-1]
        for j in range(len(l)-1, 0, -1):
            x = 1/x + l[j-1]
        return x


def dec_to_chain(num):
    x = num // 1
    return int(x)


def chain_to_frac(l):
    x, y = 1, l[len(l)-1]
    for i in range(len(l)-1, 0, -1):
        temp = x
        x = y
        y = l[i-1] * y + temp
        x, y = simp([x, y])[0], simp([x, y])[1]
    return [y, x]


def best_frac_below(num, limit):
    x = math.sqrt(num)
    cfrac = []
    frac = [1, 1]
    denom = 0
    if x % 1 != 0:
        while frac[1] <= limit:
            denom = int(frac[1])
            cfrac.append(x//1)
            x = 1 / (x - x//1)
            frac = simp(chain_to_frac(cfrac))
            # vi skal bruge en ny "while" der tjekker hele vejen op til tallet..? Lyder langt
    print("fra %s fik vi %s" % (num, denom))
    return denom


n = 100
s = 0

for i in range(13, 13 + 1):
    s += best_frac_below(i, n)

print(s)

stop = timeit.default_timer()
print(stop - start)
