grid = []

i = 0
with open('../../resources/11.txt') as text:
    for line in text:
        grid.append(line.split())
        i += 1

for i in range(20):
    for j in range(20):
        grid[i][j] = int(grid[i][j])

max = 0
index = [0, 0]
direction = "Ukendt"

# Horizontally
i = 0
while i < 20:
    j = 0
    while j + 3 < 20:
        prod = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        j += 1
        if prod > max:
            max = prod
            index = [i, j - 1]
            direction = "horizontally"
    i += 1

j = 0
while j < 20:
    i = 0
    while i + 3 < 20:
        prod = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        i += 1
        if prod > max:
            max = prod
            index = [i - 1, j]
            direction = "vertically"
    j += 1

i = 0
while i + 3 < 20:
    j = 0
    while j + 3 < 20:
        prod = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        j += 1
        if prod > max:
            max = prod
            index = [i, j - 1]
            direction = "diagonally down"
    i += 1

i = 19
while i - 3 >= 0:
    j = 0
    while j + 3 < 20:
        prod = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
        j += 1
        if prod > max:
            max = prod
            index = [i, j - 1]
            direction = "diagonally up"
    i -= 1

print(grid[index[0]][index[1]])
print(max, index, direction)
