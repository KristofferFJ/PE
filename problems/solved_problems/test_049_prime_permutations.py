# PRIME PERMUTATIONS

from library.primes import primes_bool_up_to

pl = primes_bool_up_to(10000)
list = [p for p in range(1000, 10000) if pl[p]]


def anagram(n, m):
    a, b = str(n), str(m)
    value = True
    for i in range(10):
        if a.count(str(i)) != b.count(str(i)):
            value = False
    return value


for i in range(0, len(list)-2):
    for j in range(i + 1, len(list)-1):
        if anagram(list[i], list[j]):
            progression = list[j] - list[i]
            dif = 0
            k = j+1
            while k < len(list) and dif < progression:
                dif = list[k] - list[j]
                if dif == progression and anagram(list[j],list[k]):
                    print("SUCCES med prog=%s, %s, %s og %s" % (progression, list[i], list[j], list[k]))
                else:
                    k += 1
