# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 07:15:37 2019

@author: ymamo

Adapted from Python for Engineers at 
pythonforengineers.com/analysing-the-enron-email-corpus/
"""

import os
from email.parser import Parser


#Link to directory of information
#only look at a small part of the data to debug and test your code
rootdir = ".\\maildir\\lay-k\\family"

#Helper function to move the data into my selected data structure
def email_analyse(inputfile, to_email_list, from_email_list, email_body):
    with open(inputfile, "r") as f:
        data = f.read()  # reads the file
 
    email = Parser().parsestr(data) 
 
    to_email_list.append(email['to'])
    from_email_list.append(email['from'])
 
    email_body.append(email.get_payload())
    
    
#empty lists to structure the data!!!
to_email_list = []
from_email_list = []
email_body = []

'''

PART 1: Use Helper Function to move data from unstructured email form to 
structured form

'''

print ("moving data to new structures")
for directory, subdirectory, filenames in  os.walk(rootdir):
    for filename in filenames:
        #uses the root directory
        #see files
        email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body )


'''

PART 2: Move newly structured data into files, in this case .txt
there are other types like pickle files, binaries, csvs etc

'''

#Move "to_email_list
print ("saving to email list as text \n")
with open("to_email_list.txt", "w") as f:
    for to_email in to_email_list:
        if to_email: #if there is to email then write (avoids adding empty lines)
            f.write(to_email)
            f.write("\n")

#Moves from_email list
print ("saving from email list as text \n")
with open("from_email_list.txt", "w") as f:
    for from_email in from_email_list:
        if from_email: #if there is an from email then write (avoids adding empty lines)
            f.write(from_email)
            f.write("\n")        

#Moves email body
print ("saving email body as text \n")
with open("email_body.txt", "w") as f:
    for email_bod in email_body:
        if email_bod: #if there is an email body then write (avoids adding empty lines)
            f.write(email_bod)
            f.write("\n")  
    

#Let's look at the text files and see what we got
            
# Issues are in the lay-k/family folder, open up the file 4
    