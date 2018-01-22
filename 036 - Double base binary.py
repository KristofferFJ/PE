#DOUBLE-BASE PALINDROMES
#Find palindromer, der både er palindrom i base 2 og base 10.

def dec_to_bin(n):
	return int(bin(n)[2:])
	
def is_palindrome(n):
	list = [i for i in str(n)]
	if list == list[::-1]:
		return True

count = 0	
sum = 0	
for i in range(1,10**9):
	if is_palindrome(i):
		if is_palindrome(dec_to_bin(i)):
			print (i)
			print (dec_to_bin(i))
			count += 1
			sum += i
			
print (count)
print (sum)