#MULTIPLES AF 3 og 5

n = int(input("Multiplum af "))
m = int(input("Og "))
num = int(input("Mindre end "))
sum = 0

for i in range(1,num):
    if n * i % m and n * i < num:
        sum += n*i
    if m * i < num:
        sum += m*i

print (sum)
