# EVEN FIBONACCI NUMBERS

Fibonacci = [1,1]
n = 0
i = 0

while n < 4000000 and i<4000000:
    n = Fibonacci[i] + Fibonacci[i+1]
    Fibonacci.append(n)
    i += 1

Even_Fibonacci = Fibonacci[2::3]	

s = 0
for i in range(len(Even_Fibonacci)):
    s += Even_Fibonacci[i]

print (s)