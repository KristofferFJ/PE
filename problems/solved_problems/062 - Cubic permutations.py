# Find det mindste kubiktal, for hvilket præcis 5 af dens permutationer er kubiktal.

import time

start = time.time()

permutations_required = 5
permutations = {}

num = 0
while True:
    num += 1
    cube = num**3
    smallest_permutation = int("".join(sorted(str(cube))[::-1]))
    if smallest_permutation in permutations:
        permutations[smallest_permutation].append(num)
        if len(permutations[smallest_permutation]) == permutations_required:
            print("Hurra")
            print(permutations[smallest_permutation])
            print([i**3 for i in permutations[smallest_permutation]])
            break
    else:
        permutations.update({smallest_permutation: [num]})


print(time.time() - start)
