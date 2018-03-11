#67 - Maximum path s II

from math import *

numbers = open("triangle.txt","r")
grid = []

for line in numbers:
	grid.append(line.split())
	
for i in range(len(grid)):
	for j in range(len(grid[i])):
		grid[i][j] = int(grid[i][j])

i = len(grid)-2
while i >= 0:
	print ("i er " + str(i))
	j = 0
	while j < len(grid[i]):
		grid[i][j] += max(grid[i+1][j], grid[i+1][j+1])
		j += 1
	i -= 1