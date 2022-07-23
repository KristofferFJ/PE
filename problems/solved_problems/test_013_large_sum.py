#13 - Large s
s = 0
with open('../../resources/13.txt') as numbers:
	for line in numbers:
		s += int(line)
	print(s)
	