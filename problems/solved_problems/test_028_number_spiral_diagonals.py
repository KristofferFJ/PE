# Find summen af diagonalerne i en talspiral.

s = 1
for i in range(1,501):
    s += 2*(2*(i*2+1)**2 - 6*i)

print(s)
