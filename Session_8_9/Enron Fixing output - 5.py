# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:35:46 2019

@author: ymamo

Adapted from Python for Engineers at 
pythonforengineers.com/analysing-the-enron-email-corpus/
"""


import os
from collections import Counter
import time

from email.parser import Parser
rootdir = ".\\maildir\\lay-k\\family" #Round One
#rootdir = ".\\maildir\\lay-k" #Round Two --DO NOT WIRTE TO FILE see below (takes forever)
#rootdir = ".\\maildir" #Round three --ONLY WRITE EMAIL TEXT TO FILE (takes forever)


def email_analyse(inputfile, to_email_list, from_email_list, email_body):
    with open(inputfile, "r") as f:
        data = f.read()

    email = Parser().parsestr(data)
    
    #This correct the issues we Enron Structuring 4 and put all emails on  
    #their own line
    
    if email['to']:
        email_to = email['to']
        email_to = email_to.replace("\n", "")
        email_to = email_to.replace("\t", "")
        email_to = email_to.replace(" ", "")

        email_to = email_to.split(",")

        for email_to_1 in email_to:
            to_email_list.append(email_to_1)

    from_email_list.append(email['from'])

    email_body.append(email.get_payload())


to_email_list = []
from_email_list = []
email_body = []

start = time.time()

for directory, subdirectory, filenames in  os.walk(rootdir):
    for filename in filenames:
        email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body )

print("\nTo email adresses: \n")
print(Counter(to_email_list).most_common(10)) #From Collections counts number of same items

print("\nFrom email adresses: \n")
print(Counter(from_email_list).most_common(10)) #From Collections counts number of same items

print ("The number of emails = ", len(email_body))
           
#''' add these for round 2 and 3
with open("to_email_list.txt", "w") as f:
    for to_email in to_email_list:
        if to_email:
            f.write(to_email)
            f.write("\n")
with open("from_email_list.txt", "w") as f:
    for from_email in from_email_list:
        if from_email:
            f.write(from_email)
            f.write("\n")        
   

with open("email_body.txt", "w") as f:
    for email_bod in email_body:
        if email_bod:
            f.write(email_bod)
            f.write("\n")
'''# add these for round 2 and 3
             
print ("\nTime took to parse: ", time.time() -start )



