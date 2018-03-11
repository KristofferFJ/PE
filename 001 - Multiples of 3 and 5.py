# MULTIPLES AF 3 og 5

n = int(input("Multiplum af "))
m = int(input("Og "))
num = int(input("Mindre end "))
s = 0

for i in range(1,num):
    if n * i % m and n * i < num:
        s += n*i
    if m * i < num:
        s += m*i

print(s)
