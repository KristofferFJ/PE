#PROBLENM 65 - CONVERGENTS OF E

def gcd(x, y):
	while (y != 0):
		x, y = y, x % y
	return x

def simp(list):
	x = int(list[0])
	y = int(list[1])
	x //= gcd(x, y)
	y //= gcd(x, y)
	return [x, y]
	
def chain_to_dec(list):
		x = list[len(list)-1]
		for i in range(len(list)-1,0,-1):
			x = 1/x + list[i-1]
		return x

def dec_to_chain(num):
	x = num // 1
	return int(x)
		
def chain_to_frac(list):
	temp = 1
	x, y = 1, list[len(list)-1]
	for i in range(len(list)-1,0,-1):
		temp = x
		x = y
		y = list[i-1] * y + temp
		x, y = simp([x,y])[0], simp([x,y])[1]
	return [y, x]

e = [2]
for i in range(1,34):
	e.append(1)
	e.append(2*i)
	e.append(1)

print (e)
	
#e = [2,1,2,1,1,4,1,1,6,1,1,8,1,1,10,1,1,12,1,1,14,1,1,16,1,1,18,1,1,20,1,1,22,1,1,24,1,1,26,1,1,28,1,1,30,1,1,32,1,1,34,1,1,36,1,1,38,1,1,40,1,1,42,1,1,44,1,1,46,1,1,48,1,1,50,1,1,52,1,1,54,1,1,56,1,1,58,1,1,60,1,1,62,1,1,64,1,1,66,1]

a = chain_to_frac(e)
b = s(int(i) for i in str(a[0]))

print (b)
