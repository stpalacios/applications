# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:56:53 2019

@author: ymamo

Adapted from Python for Engineers at 
pythonforengineers.com/analysing-the-enron-email-corpus/

"""


'''
First we need to extract the data and it is not small.
Let's see how long it takes
'''

import tarfile #library to aid the extraction
import time #native library to see how long it takes

start = time.time()
tf = tarfile.open("enron_mail_20150507.tgz") # store the file as an object
tf.extractall() #use the tarfile method to extract
end = time.time() - start

print ("Extraction took: ", end, "\n" )
