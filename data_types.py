"""
Python has five standard data types

Immutable Data types
    * String 
    * Numbers 
    * Tuple 
    * frozen set
    * Boolean
    * array
    * bytes
    
Mutable Data types
    * List 
    * Dictionary
    * Set 
    * byte array
"""
#-----------------------------------------------------------------------------------------------------------------------
# Numbers (int,long,float,complex)

a = 2
print(type(a)) #int

"""
    b= 343434L     #long  [Not supported in version 3]
    print(type(b))
"""

c= 5.5         #float
print(type(c))

d = 5+6j       #complex
print(type(d))

#-----------------------------------------------------------------------------------------------------------------------
# String
s1= 'Dhoni'

s2= "Dhoni is the best person"

s3= """Dhoni is the best wk in the world.
       He is also good in batting.
       He is my best.
"""
# string subsets
print(s1[:-1])  #where begin with 0 and end at -1

#-----------------------------------------------------------------------------------------------------------------------
# List
l1 = ['dhoni',23,85.7,True]  #suport multiple datatypes
l2 = ['married','cricketer']

print(l1+l2) #list concatenated
print(l1 *3) #list repetition

# Tuple
t1= ('dhoni',23)

#-----------------------------------------------------------------------------------------------------------------------
# Dictionary

d1={'name':'dhoni','age':23}  #consits of key-value pair, key always unique

#-----------------------------------------------------------------------------------------------------------------------
#Set

k1= [1,2,3,3,2]
s1=set(k1)
print(s1)
s1.add("set are mutable")

#Frozen set
f1 = frozenset(k1)
print(f1)
#f1.add('frozen set are immutable')

#-----------------------------------------------------------------------------------------------------------------------
# bytes
print(type(b'test')) #bytes

# array         concept not clear
variable = []
print(type(variable))

# bytes array
# Python 3
key = bytes([0x13, 0x00, 0x00, 0x00, 0x08, 0x00])

# Python 2
key = ''.join(chr(x) for x in [0x13, 0x00, 0x00, 0x00, 0x08, 0x00])

#-----------------------------------------------------------------------------------------------------------------------