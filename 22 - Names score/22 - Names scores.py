#22 - Names scores
import time


text = open("names.txt", "r")
names = []
for name in text:
	names = name.split(",")

names.sort()

def char_score(char):
	return ord(char) - 64

sum = 0
for i in range(len(names)):
	score = 0
	for j in range(1,len(names[i])-1):
		score += char_score(names[i][j])
	score *= (i+1)
	sum += score