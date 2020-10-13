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
import json





#rootdir = ".\\maildir\\lay-k\\family" #Round One
rootdir = ".\\maildir" #Round Two --DO NOT WIRTE TO FILE see below (takes forever)


def email_analyse(inputfile, email_data):
    with open(inputfile, "r") as f:
        data = f.read()

    email = Parser().parsestr(data)
    
    #This correct the issues we had Enron Structuring 4 and put all emails on  
    #their own line
    
    if email['to']:
        email_to = email['to']
        email_to = email_to.replace("\n", "")
        email_to = email_to.replace("\t", "")
        email_to = email_to.replace(" ", "")

        email_to = email_to.split(",")

        #for email_to_1 in email_to:
        #    email_data['to_email'].append(email_to_1)

        email_data["to_email"].append(email_to)
        
    else:
        email_data["to_email"].append([])
    
    email_data['from_email'].append(email['from'])

    email_data['email_body'].append(email.get_payload())


email_data = {'to_email': [], "from_email":[], "email_body":[]}
count = 1
start = time.time()
corrupt = ["delainey-d", "forney-j", "lay-k", "skilling-j"]

for directory, subdirectory, filenames in  os.walk(rootdir):
    
    for filename in filenames:
        print (directory, subdirectory, filenames)
        if filename in corrupt: 
            print (filename)
            email_analyse(os.path.join(directory, filename), email_data)
    
        #due to the size of data I am going to split into files
    if len(email_data["email_body"]) >= 34000:
        name = "emails_" + str(count) + ".json"
        count += 1 #update counter for next round
        with open(name, 'w') as file:
            json.dump(email_data, file)
        #reset dictionary
        email_data = {'to_email': [], "from_email":[], "email_body":[]}     
        print (name)

name = "emails_" + str(count) + ".json"
with open(name, 'w') as file:
   json.dump(email_data, file)


parse = time.time() 
print ("\nTime took to parse: ", parse-start )


 

