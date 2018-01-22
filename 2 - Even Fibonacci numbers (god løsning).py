#EVEN FIBONACCI NUMBERS

x, y = 1, 1
sum = 0

while x < 4000000:
	if x % 2 == 0:
		sum += x
	x, y = y, x + y

print (sum)