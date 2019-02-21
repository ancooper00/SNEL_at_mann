import os

#key is the key given in a hidden message
key = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "

#opens and reads each file and saves in string calle "content"
def get_content(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    return content

#function that replaces the old character with its proper decoded one
def find_and_replace_character(content):
    result = ""
    for w in content:
        new = key.find(w) + 32
        character = chr(new)
        result += character
    return result

#makes a new file for each decrypted message
def make_decrypted_file(decrypted, n):
    with open('file.txt', 'w') as f:
        f.write(decrypted)
    os.rename('file.txt', 'new_file_' + str(n) + '.txt')

    
#list containing remaining suspicious files
files = ["file_0AA7.txt", "file_0D01.txt", "file_1C67.txt", "file_1F87.txt",
"file_2A62.txt", "file_21C1.txt", "file_30D3.txt", "file_063D.txt", "file_340B.txt", 
"file_0936.txt", "file_2715.txt"]

n = 0

for f in files:
    content = get_content("/Users/acoope9015/Desktop/SNEL/suspicious_files/"+f)
    decrypted = find_and_replace_character(content)
    new_file = make_decrypted_file(decrypted, n)
    n += 1
    


    
    
