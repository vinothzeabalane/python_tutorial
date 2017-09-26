"""
 Iterator:
   Python iterator objects are required to support two methods while following the iterator protocol.

__iter__ returns the iterator object itself. This is used in for and in statements.

__next__ method returns the next value from the iterator. If there is no more items to return then it should raise StopIteration exception.

"""
x = iter([1,2,3])
print( next(x))


"""
Generator:
    Generators simplifies creation of iterators. A generator is a function that produces a sequence of results instead of a single value.
"""
def yrange(n):
    i=0
    while i <n:
        yield i
        i += 1

res = yrange(5)

print(next(res))
print(next(res))