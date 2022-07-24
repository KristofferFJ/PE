import string
import unittest

from library.common import Common
from library.permutations import Permutations

"""
XOR decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII 
(American Standard Code for Information Interchange). 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, 
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. 
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", 
it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters. 
Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text.
"""

characters = string.ascii_lowercase
possible_keys = Permutations.combinations_of_length_3(characters)
encrypted_text = [int(i) for i in Common.read_from_resources("59").read().split(",")]
banned_letters = ["~", "{", "$", "@", "%", "!"]


def find_encrypted_text():
    for possible_key in possible_keys:
        cipher_ascii = ""
        text = encrypted_text
        for i in range(0, len(text)):
            j = i % len(possible_key)
            xor = text[i] ^ ord(possible_key[j])
            cipher_ascii = cipher_ascii + chr(xor)
            if len([bad_letter for bad_letter in banned_letters if bad_letter in chr(xor)]) > 0:
                break
        if len(cipher_ascii) == len(encrypted_text):
            return cipher_ascii


class Test(unittest.TestCase):
    def test_decrypt(self):
        encrypt = 65 ^ 42
        assert encrypt == 107
        assert encrypt ^ 42 == 65

    def test_result(self):
        print(sum([ord(letter) for letter in find_encrypted_text()]))
