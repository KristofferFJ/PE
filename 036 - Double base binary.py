# DOUBLE-BASE PALINDROMES
# Find palindromer, der både er palindrom i base 2 og base 10.


def dec_to_bin(n):
    return int(bin(n)[2:])


def is_palindrome(n):
    digit_list = [i for i in str(n)]
    if digit_list == digit_list[::-1]:
        return True


count = 0	
s = 0	
for i in range(1, 10**9):
    if is_palindrome(i):
        if is_palindrome(dec_to_bin(i)):
            print(i)
            print(dec_to_bin(i))
            count += 1
            s += i

print(count)
print(s)
