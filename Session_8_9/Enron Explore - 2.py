# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:51:35 2019

@author: ymamo

Adapted from Python for Engineers at 
pythonforengineers.com/analysing-the-enron-email-corpus/

"""
# import operating system library
import os

#identify a folder to explore, store as variable rootdir
rootdir = ".\\maildir"
count_emails = 0
#iterate through each director and print 
for directory, subdirectory, filenames in os.walk(rootdir):
    count_emails += len(filenames)
    #print(directory, subdirectory, len(filenames))
    
print (count_emails)