#571 - SUPER PANDIGITAL NUMBERS
#Find et tal, der indeholder alle cifre (ikke kun én gang) i alle
#talsystemer fra 2 til n.
#10 mindste 12-super-pandigital tal.

def base_conv(n,base):
	num = 0
	while n != 0:
		pot = 0
		while base**(pot+1) <= n:
			pot += 1
		coef = 1
		while (coef+1)*(base**pot) < n:
			coef += 1
		num += coef*(10**pot)
		n -= coef*(base**pot)
	return num
	
"""def pan_check(n,base):
	pan = True
	for i in range(base):
		if not str(i) in str(n):
			pan = False
			break
	return pan"""
	
#Ovenstående er super langsomt.. Bummelum
	
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
	
def pan_check(list,base):
	check = True
	for i in range(base):
		if i not in list:
			check = False
			break
	return check
	
count = 0
s = 0
j = 12**11
while count < 10:
	pan = True
	for i in range(2,12):
		if not pan_check(numberToBase(j,i),i):
			pan == False
			break
	if pan == True:
		count += 1
		s += j
		print ("Vi fandt "+str(j))
	j += 1

	
	