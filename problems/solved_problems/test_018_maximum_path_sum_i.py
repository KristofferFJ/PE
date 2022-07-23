#18 - Maximum Path s I
from math import *

numbers = open("../../resources/18.txt", "r")
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
	
"""	
#BRUTE FORCE metode herunder.
s = 0

for a in range(1):
	for b in range(a, a+2):
		for c in range(b, b+2):
			for d in range(c, c+2):
				for e in range(d, d+2):
					for f in range(e, e+2):
						for g in range(f, f+2):
							for h in range(g, g+2):
								for i in range(h, h+2):
									for j in range(i, i+2):
										for k in range(j, j+2):
											for l in range(k, k+2):
												for m in range(l, l+2):
													for n in range(m, m+2):
														for o in range(n, n+2):
															temp = (grid[0][a]+grid[1][b]+grid[2][c]+grid[3][d]+grid[4][e]+
																	grid[5][f]+grid[6][g]+grid[7][h]+grid[8][i]+grid[9][j]+
																	grid[10][k]+grid[11][l]+grid[12][m]+grid[13][n]+grid[14][o])
															if temp > s:
																s = temp
																print (("Maks er stien: %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s") % 
																	(grid[0][a],grid[1][b],grid[2][c],grid[3][d],grid[4][e],
																	grid[5][f],grid[6][g],grid[7][h],grid[8][i],grid[9][j],
																	grid[10][k],grid[11][l],grid[12][m],grid[13][n],grid[14][o]))"""