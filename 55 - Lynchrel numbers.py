#LYNCHREL NUMBERS
#Tal, der når vi lægger dem sammen med de omvendte bliver palindromer.

def is_palindrome(n):
	list = [int(i) for i in str(n)]
	if list == list[::-1]:
		return True
	else:
		return False

def flip_sum(n):
	list = [int(i) for i in str(n)]
	m = 0
	for i in range(len(list)):
		m += (10**i)*list[i]
	return m

count = 0
for i in range(10000):
	k = i
	Lyncrel = True
	for j in range(50):
		i = i + flip_sum(i)
		if is_palindrome(i):
			Lyncrel = False
			break
	if Lyncrel:
		count += 1
		print (k)

print (count)