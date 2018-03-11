import timeit
start = timeit.default_timer()


def is_palindrome(n):
    num = str(n)
    num_list = [int(x) for x in num]
    if num_list == num_list[::-1]:
        return True
    else:
        return False


def find_largest_palindrome(n):
    palindrome = 1
    while n > 0:
        m = n
        while m > 0:
            if is_palindrome(m * n):
                if palindrome < m * n:
                    palindrome = m * n
                print ("Palindrome fundet ved %s * %s" % (m, n))
                break
            else:
                m -= 1
        n -= 1
    print ("Det største blev %s" % palindrome)


find_largest_palindrome(999)
stop = timeit.default_timer()
print (stop - start)