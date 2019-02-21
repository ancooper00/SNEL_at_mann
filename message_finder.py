
#changes the hex file naming system to a decimal system
def get_file_name(n):
     number = str(hex(n))
     num_no_lead = number[2:]
     num_zero = 4 - len(num_no_lead)
     
     for n in range(num_zero):
          num_no_lead = "0" + num_no_lead
          
     return 'file_' + num_no_lead + '.txt'

#opens and read each file saving the content in a string called "content"
def get_content(file_name):
     with open(file_name, 'r') as f:
          content = f.read()
     return content

#counts each type of character and puts it in a list called counts
def count_characters(text):
     counts = [0] * 127

     for n in text:
          i = ord(n)
          counts[i] += 1
          
     return counts[32:]

#function to calculate chi squared of each file      
def chi_squared(nums):
    expected = sum(nums) / len(nums)
    numerator_total  = 0
    for i in nums:
        numerator_total += (i - expected)**2
    return numerator_total / expected


#algorithm that runs through each of the above functions to return files with suspicious chi square value
num_files = 18000
threshold = 150

for n in range(num_files):
     file_name = get_file_name(n)
     text = get_content("text_files/"+file_name)
     counts = count_characters(text)
     chi_square = chi_squared(counts)


     if chi_square > threshold:
          print(file_name , chi_square)
     
     

    
    
