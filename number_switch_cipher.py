import os

#opens and reads each file
def get_content(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    return content

#function that replaces each character by proper shift given in the
#clue about the number switch (32 switches with 126, etc)
def find_and_replace_character(content):
    result = ""
    for w in content:
        new = 158 - ord(w)
        result += chr(new)
        
    return result

#writes new file with decrypted message
def make_decrypted_file(decrypted, n):
    with open('file.txt', 'w') as f:
        f.write(decrypted)
    os.rename('file.txt', 'new_file_' + str(n) + '.txt')

    
#list containing remaining suspicious files
files = ["file_0AA7.txt", "file_0D01.txt", "file_1C67.txt", "file_1F87.txt",
"file_2A62.txt", "file_21C1.txt", "file_30D3.txt", "file_063D.txt", "file_340B.txt", 
"file_0936.txt"]


#algorithm to run read and decrypte files
n = 0

for f in files:
    content = get_content("/Users/acoope9015/Desktop/SNEL/number_switch_files/"+f)
    decrypted = find_and_replace_character(content)
    new_file = make_decrypted_file(decrypted, n)
    n += 1
    
    



    
    
