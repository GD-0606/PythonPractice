"""
    different types of arrays in Numpy 
    1.0-d
    2.1-d
    3.2-d
    4.3-d
"""
import numpy as np
a=np.array(24)

b=np.array([1,2,3,4,"gopi"])
c=np.array([[1,2,3,4],[5,6,7,8]])
d=np.array([[[1,2]]])

print(a.ndim,b.ndim,c.ndim,d.ndim,a,b)

e=np.array([1,2],ndmin=5)
print(e)

# using the arange() - only 1-d array is possible.

nd1=np.arange(1,5,2)
print(nd1)

# using zeros()

nd2=np.zeros((2,3))

print(nd2)

#using ones()

nd3=np.ones((12))
print(nd3)
#using full()
nd4=np.full((2,2,3),6)

print(nd4)

#using identity()

nd5=np.identity(4)
print(nd5)