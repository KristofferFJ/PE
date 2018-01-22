list_of_primes = [x for x in range(2,1000)]

#SUM OF SQUARES OG SQUARE OF SUM
n = int(input("Vælg tal "))

def square_of_sum(n):
	return int((n*(n+1)/2) ** 2)

def sum_of_squares(n):
	sum = 0
	for i in range(n):
		sum += (i+1) ** 2
	return sum

print (square_of_sum(n))
print (sum_of_squares(n))
print (square_of_sum(n) - sum_of_squares(n))
