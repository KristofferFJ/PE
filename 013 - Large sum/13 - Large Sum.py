#13 - Large s
s = 0
with open('s.txt') as numbers:
	for line in numbers:
		s += int(line)
	