#lambda
from _functools import reduce

l1=lambda x : x**2
print(l1(2))

#------------------------------------------------------------------------------------------------------------------
#map

def square(x):
    return x**2

items = [1, 2, 3, 4, 5]

res = list(map(square,items))
print(res)

#------------------------------------------------------------------------------------------------------------------
#filter

res1= list(filter(lambda x :  x % 2 == 0 ,items))
print(res1)

#------------------------------------------------------------------------------------------------------------------
#reduce

res2= reduce(lambda x,y: x+y, items)
print(res2)

#------------------------------------------------------------------------------------------------------------------
#list comprehension

res3 = [x**2 for x in range(5)]
print(res3)

#------------------------------------------------------------------------------------------------------------------