import timeit
start = timeit.default_timer()


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_list():
    s1 = 1
    s2 = 1
    count = 2
    while len(str(s1)) < 1000:
        temp = s1
        s1 = s1 + s2
        s2 = temp
        count += 1
    return count


print(fibonacci_list())
print(timeit.default_timer() - start)
