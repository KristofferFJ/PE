# 38 - Pandigital multiples

rec = 0

for i in range(10000):
    prods = str(i)
    mult = 2
    while len(prods) < 9:
        prods = prods + str(mult*i)
        mult += 1
    if "".join(sorted(prods)) == "123456789" and int(prods) > rec:
        print(prods)
        rec = int(prods)
