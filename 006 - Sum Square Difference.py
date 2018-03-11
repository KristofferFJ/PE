list_of_primes = [x for x in range(2,1000)]

# s OF SQUARES OG SQUARE OF s
n = int(input("Vælg tal "))


def square_of_s(n):
    return int((n*(n+1)/2) ** 2)


def s_of_squares(n):
    s = 0
    for i in range(n):
        s += (i+1) ** 2
    return s


print (square_of_s(n))
print (s_of_squares(n))
print (square_of_s(n) - s_of_squares(n))
