'''
Created on Jun 24, 2018

@author: ozeabalx
'''
import yaml
document = """
  a: 1
  b:
    c: 3
    d: 4
"""
print (yaml.dump(yaml.load(document)))


 
with open(r"C:\Users\ozeabalx\Desktop\python-sesion\config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
  
for section in cfg:
    print(section)
      
print(cfg['mysql'])
print(cfg['other'])