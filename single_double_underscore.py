"""
single = internal

double = Private

"""

class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"
        
mc = MyClass()
print(mc.__superprivate)