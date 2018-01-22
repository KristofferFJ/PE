#42 - Coded triangle numbers

text = open("words.txt","r")
words = []
for line in text:
	words = [word.strip('"') for word in line.split(",")]
	
triangle_numbers = set([int(i*(i+1)/2) for i in range(1,20)])

s = 0
for word in words:
	if sum([(ord(letter)-64) for letter in word]) in triangle_numbers:
		print (word)
		s += 1
