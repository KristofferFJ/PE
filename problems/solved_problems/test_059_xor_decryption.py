#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

numbers = open("../../resources/59.txt", "r")

grid = []
for line in numbers:
	grid = line.split(",")

alphabet = 'abcdefghijklmnopqrstuvxyz'
potential_keys = []
for letter1 in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            potential_keys.append(letter1 + letter2 + letter3)

numbers = [int(a) for a in grid]
stuff = [chr(97^a) for a in numbers]

def validate(number):
    if(number < 65):
        return False
    if(number > 90 and number < 97):
        return False
    if(number > 122):
        return False
    return True

def decrypt(numbers, key):
    result = ''
    index = 0
    for number in numbers:
        this_key = key[index]
        decrypted_number = number^ord(this_key)
        result += chr(decrypted_number)
        index = (index + 1) % 3
    return result

for character in alphabet:
    result = ''
    index = 0
    for number in numbers:
        if index % 3 == 0:
            decrypted_number = number^ord(character)
            result += chr(decrypted_number)
        index = index + 1
    print (result)