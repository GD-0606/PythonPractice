# attributes for ndarray object
import numpy as np
nd3=np.array([[1,2,3],[1,2,3],[4,5,6],[1,2,3]])

print(nd3)

print(nd3.ndim)

print(nd3.shape)

print(nd3.size)

print(nd3.dtype)

print(nd3.itemsize) # The size (in bytes) of each element in the array.

print(nd3.nbytes)  # The total number of bytes consumed by the elements of the array.
print(nd3.T)
print(nd3.data)