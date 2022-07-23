# 32 - Pandigital products

# Løst ved nedenstående.
# Bedre idé fra PE: Brug sorted på en string og tjek om
# den er lig "123456789".

numbers = set([])


def check_pan(num):
    n = str(num)
    if len(n) == 9:
        if (("1" in n) and ("2" in n) and ("3" in n) and ("4" in n)
           and ("5" in n) and ("6" in n) and ("7" in n) and ("8" in n) and ("9" in n)):
            return True
    else:
        return False


for i in range(5000):
    print("i er nu" + str(i))
    lower_bound = 10**(4-len(str(i)))
    upper_bound = lower_bound * 9 + 1
    for j in range(lower_bound, upper_bound):
        s = str(i) + str(j) + str(i*j)
        if check_pan(int(s)):
            numbers.add(i*j)
