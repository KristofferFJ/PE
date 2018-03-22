# INTEGER RIGHT TRIANGLES: For et heltal x, hvor mange rette trekanter findes der
# med omkreds x? Find x med flest hvor x <= 1000.


def check_right(a, b, c):
    if c**2 == b**2 + a**2:
        return True
    else:
        return False


p = 4
max = 0
maxp = 1
while p <= 1000:
    print ("Vi tjekker p = %s" % p)
    count = 0
    a = b = 1
    while a <= int(p*(1/3)):
        b = a
        c = p - a - b
        while c > b:
            if c**2 == b**2 + a**2:
                count += 1
            b += 1
            c -= 1
        a += 1
    if count > max:
        maxp = p
        max = count
    p += 1

print(maxp)
