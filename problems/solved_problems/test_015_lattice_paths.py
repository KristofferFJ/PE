# 15 Lattice paths:
# Handler om hvor mange veje, der er i et 20x20 grid hvis man kun må gå ned ad.
# Kender formlen, laver bare factorial for sjov.


def fact(n):
    res = 1
    if n == 1:
        return res
    else:
        return n*fact(n-1)


def paths_in_grid(n,m):
    return int(fact(n+m)/(fact(n)*fact(m)))


print (paths_in_grid(20,20))