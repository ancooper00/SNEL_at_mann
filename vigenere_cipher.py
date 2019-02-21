#Vigenere cipher


import os

# function that creates  a key of the length of the encrypted message out of the keyword
def make_key(keyword, message_length):
     
    key = "enigma" * (message_length // len(keyword))

    return key

#function that makes a new decrypted string following the shift and rules for the vigenere cipher
def vigenere(content, key):
    result = ""
    i = 0

    while i < 18000:

        coded_letter = content[i]
        key_letter = key[i]
        
        new = ord(coded_letter) - ord(key_letter)
        
        while new < 32:
            new = new + 95
        result += chr(new)

        i += 1
        
    return result

#opens and reads each file
def get_content(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    return content

#function that writes a new file for each decrypted message
def make_decrypted_file(decrypted, n):
    with open('file.txt', 'w') as f:
        f.write(decrypted)
    os.rename('file.txt', 'new_file_' + str(n) + '.txt')

#list containing remaining suspicious files    
files = ["file_0AA7.txt", "file_0D01.txt", "file_1F87.txt", "file_2A62.txt", "file_21C1.txt" , "file_30D3.txt", "file_340B.txt" , "file_0936.txt" ]

#variables for decryption
n = 0
keyword = "enigma"
message_length = 18000

#algorithm for running through reading, decrypting, and writing
for f in files:
    content = get_content("/Users/acoope9015/Desktop/SNEL/suspicious_files/"+f)
    key = make_key(keyword, message_length)
    decrypted = vigenere(content, key)
    new_file = make_decrypted_file(decrypted, n)
    n += 1
    
