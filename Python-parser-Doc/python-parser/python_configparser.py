'''
Created on Jun 24, 2018

@author: ozeabalx
'''

import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45','Compression': 'yes','CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open(r"C:\Users\ozeabalx\Desktop\python-sesion\example.ini", 'w') as configfile:
    config.write(configfile)
print("Execution completed.....")



config.sections()
config.read(r"C:\Users\ozeabalx\Desktop\python-sesion\example.ini")
print config.sections()
print config['bitbucket.org']['User']
print config['DEFAULT']['Compression']