# LYNCHREL NUMBERS
# Tal, der når vi lægger dem sammen med de omvendte bliver palindromer.


def is_palindrome(n):
    number_list = [int(i) for i in str(n)]
    if number_list == number_list[::-1]:
        return True
    else:
        return False


def flip_s(n):
    number_list = [int(i) for i in str(n)]
    m = 0
    for i in range(len(number_list)):
        m += (10**i)*number_list[i]
    return m


count = 0
for i in range(10000):
    k = i
    Lyncrel = True
    for j in range(50):
        i = i + flip_s(i)
        if is_palindrome(i):
            Lyncrel = False
            break
    if Lyncrel:
        count += 1
        print(k)


print(count)
