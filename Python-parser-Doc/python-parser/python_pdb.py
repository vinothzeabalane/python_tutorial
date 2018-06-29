'''
Created on Jun 26, 2018

@author: ozeabalx
'''

import configparser
import pdb

config = configparser.ConfigParser()

config.sections()
config.read(r"C:\Users\ozeabalx\Desktop\python-sesion\example.ini")
print config.sections()
pdb.set_trace()
print config['bitbucket.org']['User']
print config['DEFAULT']['Compression']
print "Execution completed....."