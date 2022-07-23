# Find det unikke heltal, der har et kvadrat på formen: 1_2_3_4_5_6_7_8_9_0.
# Når kvadratet slutter på 0, må der være 2*5 i det oprindelige tal og derfor
# (2*5)**2. De 2 sidste cifre er 00 og problemet er noget lettere at
# brute-force.

a = int(19293949596979899**.5)
b = int(10203040506070809**.5)

for i in range(b,a):
    c = str(i**2)
    if c[0]=="1" and c[2]=="2" and c[4]=="3" and c[6]=="4" and c[8]=="5" and c[10]=="6" and c[12]=="7" and c[14]=="8" and c[16]=="9":
        print ("Juhuu fundet")
        print ("%s har kvadratet %s" % (i, i**2))
        break
