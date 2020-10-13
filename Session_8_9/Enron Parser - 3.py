# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:00:12 2019

@author: ymamo

Adapted from Python for Engineers at 
pythonforengineers.com/analysing-the-enron-email-corpus/
"""

'''

"Originally, I was going to parse the file by hand (using regexes). I even wrote some code for it,
but it was hundreds of lines long.

I searched around till I found a good library to open emails in Python, and this reduced
 the code from hundreds to tens of lines."
 (https://www.pythonforengineers.com/analysing-the-enron-email-corpus/, 2019)
 '''
 
 
#Import the necessary libraries 	
from email.parser import Parser
 

#store key lay documents as variable
file_to_read = ".\\maildir\\lay-k\\all_documents\\1"

#Open the file and store it as vairbale data
with open(file_to_read, "r") as f:
    data = f.read()
    
#Use the parser library to make life easier
email = Parser().parsestr(data)


print("\nTo: " , email['to'])
print("\nFrom: " , email['from'])
 
print("\nSubject: " , email['subject'])


#AT THIS POINT LOOK AT THE FILE PATH AND EMAIL--- HOW WOULD YOU ALTER THE CODE?

#print ("\n\n", email.keys())

#How to get the body of the email--not one of the keys
#print("\n \n Body: " , email.get_payload())
 