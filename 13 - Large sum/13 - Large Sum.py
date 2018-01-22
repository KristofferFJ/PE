#13 - Large Sum
sum = 0
with open('Sum.txt') as numbers:
	for line in numbers:
		sum += int(line)
	