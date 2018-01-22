#31 - Coin sums
#Jeg brute-forcer den.
#Rækkefølgen af variable er: 1p, 2p, 5p, 10p, 20p, 50p, 1P, 2P
#Brute-force virkede, men var super ineffektivt.
"""
s = 0
for i in range(201):
	print ("i er nu "+str(i))
	for j in range(101):
		for k in range(41):
			for l in range(21):
				for m in range(11):
					for n in range(5):
						for o in range(3):
							if (i + 2*j + 5*k + 10*l + 20*m +
								50*n + 100*o == 200):
								s += 1
"""

#Lånt fra arvin på PE
coins = [ 200, 100, 50, 20, 10, 5, 2, 1 ]

def foo(rest, i = 0):
    if i == len (coins) - 1:
        return rest % coins[i] == 0
    else:
        return sum (foo (rest - j*coins[i], i + 1)
                    for j in range(rest // coins[i] + 1))

print (foo(200))