# DIGIT CANCELLING FRACTIONS:
# Find brøker, hvor man kan eliminere cifre forkert, men få
# det rigtige svar.


def dct_check(n, d):
    if d % 10 != 0 and str(n)[1] == str(d)[0]:
        if (n//10)/(d % 10) == n/d:
            return True
    elif str(n)[0] == str(d)[0] and d % 10 != 0:
        if (n % 10)/(d % 10) == n/d:
            return True
    elif str(n)[1] == str(d)[1] and str(n)[1] != "0":
        if (n//10)/(d//10) == n/d:
            return True
    elif str(n)[0] == str(d)[1]:
        if (n % 10)/(d//10) == n/d:
            return True


i = 10
count = 0
while i < 100:
    j = i + 1
    while j < 100:
        if dct_check(i, j):
            print((i, j))
            count += 1
        j += 1
    i += 1

print(count)
