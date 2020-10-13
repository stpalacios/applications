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


def email_analyse(inputfile, to_email_list, from_email_list, email_body):
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



parse = time.time() 
print ("\nTime took to parse: ", parse-start )


#import natualral language toolkit 

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#nltk.download ("punkt") required to get stopwords not necessary to do more than once


words = []

#Goes through the email body list and tokens each email
for email in email_body: 
    words += word_tokenize(email) # I use += because I don't want a list of lists
                                  #I want want a list of all the email bodies

#makes a list of uncommon words, skips the, a etc
useful_words = [word for word in words if word not in stopwords.words('English')]

#!!!!!!!!!!!!!!!Useful word exercise!!!!!!!!!!
#print (useful_words[0:10])

#gives me a distribution  of those words (i.e. a count of each time word is used)
frequency = nltk.FreqDist(useful_words)

print(frequency.most_common(100))

print ("\nTime took to nltk: ", time.time() - parse)




