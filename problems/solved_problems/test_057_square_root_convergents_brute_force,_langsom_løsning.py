import timeit
start = timeit.default_timer()


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def simp(frac_list):
    x = int(frac_list[0])
    y = int(frac_list[1])
    x //= gcd(x, y)
    y //= gcd(x, y)
    return [x, y]


def chain_to_frac(chain_list):
    x, y = 1, list[len(list)-1]
    for i in range(len(list)-1, 0, -1):
        temp = x
        x = y
        y = list[i-1] * y + temp
        x, y = simp([x, y])[0], simp([x, y])[1]
    return [y, x]


list = [1]
count = 0	
for i in range(1, 1001):
    print("Vi er kommet til "+str(i))
    list.append(2)
    frac = chain_to_frac(list)
    if len(str(frac[0])) > len(str(frac[1])):
        count += 1

print (count)
print (timeit.default_timer() - start)