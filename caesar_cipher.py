
import os

#opens and reads files, saves content into string called "content"
def get_content(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    return content

#replaces each character with new character that results from the proper shift of 32
#saves decrypted characters into string called "result"
def find_and_replace_character(content, shift):
    result = ""
    for w in content:
        new = ord(w) - shift
        if new < 32:
            new = new + 95
        result += chr(new)
    return result

#writes new file containing the decrypted string
def make_decrypted_file(decrypted, n):
    with open('file.txt', 'w') as f:
        f.write(decrypted)
    os.rename('file.txt', 'new_file_' + str(n) + '.txt')

#variables and list containing remaining suspicious files
files = ["file_0D01.txt", "file_21C1.txt", "file_063D.txt"]
n = 0
shift = 34

#algorithm to run through read, decrypting, and writing new files
for f in files:
    content = get_content("/Users/acoope9015/Desktop/SNEL/caesar_cipher/"+f)
    decrypted = find_and_replace_character(content, shift)
    new_file = make_decrypted_file(decrypted, n)
    n += 1
    
