# SQUARE ROOT CONVERGENTS
# Se på kædebrøken for 2**.5, [1,2,2,2,2,2,2...].
# De første er 1/1, 3/2, 7/5, 17/12, 41/29..
# Tydeligt mønster for både tæller og nævner: n = 2*(n-1)+(n-2)
import timeit
start = timeit.default_timer()

t2, n2 = 1, 1
t1 = 3
n1 = 2
count = 0
for i in range(3, 1001):
    n = n1*2 + n2
    t = t1*2 + t2
    if len(str(t)) > len(str(n)):
        count += 1
    t2 = t1
    n2 = n1
    t1 = t
    n1 = n

print(count)
print(timeit.default_timer() - start)
