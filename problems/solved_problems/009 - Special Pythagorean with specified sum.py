# SPECIAL PYTHAGORAS

# Vi lader som om a er 1
par = []
num = 1000
a = 1
b = 1
c = num - 2
while a < num // 3:
    print ("Vi prøver med a = %s" % a)
    while b <= c:
        if a ** 2 + b ** 2 != c ** 2:
            print ("Øv, duede ikke med %s, %s, %s" % (a,b,c))
            b += 1
            c -= 1
        else:
            print ("Fundet ved %s, %s og %s" % (a,b,c))
            par.append((a,b,c))
            break
            #exit()
    a += 1
    b = 1
    c = num - b - a
print(par)
a = 200*375*425
print(a)