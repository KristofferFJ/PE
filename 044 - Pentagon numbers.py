#44 - Pentagon numbers

import time
bignum = 10**8

pentagon_bool = [False for i in range(bignum)]

i = 1
pent = 1
while pent < len(pentagon_bool):
	pentagon_bool[pent] = True
	i += 1
	pent = int(i*(3*i-1)/2)

pentagon_numbers = []	
	
for i in range(len(pentagon_bool)):
	if pentagon_bool[i]:
		pentagon_numbers.append(i)
	
found = False
i = 1
while found == False:
	print ("tjekker " + str(pentagon_numbers[i]))
	j = 0
	while j < i and found == False:
		if (pentagon_bool[pentagon_numbers[i]+pentagon_numbers[j]]
			and pentagon_bool[pentagon_numbers[i] - pentagon_numbers[j]]):
			found = True
		j += 1
	i += 1