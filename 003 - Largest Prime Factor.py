# LARGEST PRIME FACTOR


def largest_prime(n):
    i = 2
    p = 1
    while i <= n:
        while n % i == 0:
            p = i
            n //= i
        i += 1
    return p


print (largest_prime(600851475143))