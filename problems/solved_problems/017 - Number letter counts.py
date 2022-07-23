# NUMBER LETTER COUNTS


def number_value_0(n):
    if n == 1 or n == 2 or n == 6:
        return 3
    elif n == 4 or n == 5 or n == 9:
        return 4
    elif n == 3 or n == 7 or n == 8:
        return 5
    else:
        return 0


def number_value_1(n):
    if n == 2 or n == 3 or n == 8 or n == 9:
        return 6
    elif n == 4 or n == 5 or n == 6:
        return 5
    elif n == 7:
        return 7
    else:
        return 0


def tens(n):
    if n == 11 or n == 12:
        return 6
    elif n == 13 or n == 14 or n == 18 or n == 19:
        return 8
    elif n == 15 or n == 16:
        return 7
    elif n == 17:
        return 9
    elif n == 10:
        return 3
    else:
        return 0


def combined_numbers(n):
    s = 0
    if n > 99:
        s += number_value_0(n//100)+7
        if n % 100 > 0:
            s += 3
    if (n % 100)//10 == 1:
        s += tens(n % 100)
    else:
        s += number_value_1((n % 100)//10)
        s += number_value_0(n % 10)
    return s


res = 11	
for i in range(1, 1000):
    print("%s har ordværdien %s" % (i, combined_numbers(i)))
    res += combined_numbers(i)

print (res)
