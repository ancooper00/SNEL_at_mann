
# this  renames each file to fit decimal numbering systems
def get_file_name(n):
     number = str(hex(n))
     num_no_lead = number[2:]
     num_zero = 4 - len(num_no_lead)
     
     for n in range(num_zero):
          num_no_lead = "0" + num_no_lead
          
     return 'file_' + num_no_lead + '.txt'

#opens and reads each file, saves in string called "content"
def get_content(file_name):
     with open(file_name, 'r') as f:
          content = f.read()
     return content

#creates a new file to hold the new string of first characters
def new_string_file(string):
     with open('file.txt', 'w') as f:
        f.write(string)


   
num_files = 18000
string = ""

for n in range(num_files):
     file_name = get_file_name(n)
     text = get_content("text_files/"+file_name)
     string += text[0]
    
new_string_file(string)
    
     
