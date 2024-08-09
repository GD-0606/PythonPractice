from functools import reduce 
def my_func(a,b,c,*rest,**h):
    print(a,b,c,rest,h)

my_func(1,2,9,78,j=10)

# lambda
"""
Single Executable Statement and whose Value returns 
    Automatically or Implicitly.
"""
sum=lambda a,b:a+b if a>b else a-b
print(sum(1,2))

# global variables

"""
When we want MODIFY the GLOBAL VARIABLE values in side of function defintion  
then global variable names must be preceded with 'global' keyword otherwise 
we get "UnboundLocalError: local variable names referenced before assignment.
"""
a=10
def getValue():
    global a
    print(a)
    a=a+1
getValue()
print(a)

"""
    To get the global variables across the environment we use the "global()" functions and its return type is dict
"""

"""
    special functions in python
    1.filter
    2.map
    3.reduce
"""
marks=[98,89,78,67,57]
def getAbove80(val):
    return val>80

filtered=filter(getAbove80,marks)
print(list(filtered))

def addonetomarks(mark):
    return mark+1
mapobj=map(addonetomarks,marks)
print(list(mapobj))

numbers=[1,2,3,4,5]
def getsum(acc,val):
    acc=acc+val
    return acc

total_sum=reduce(getsum,numbers,1)
print(total_sum)
