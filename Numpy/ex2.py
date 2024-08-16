# 1-d
import numpy as np
# 1-d
nd1=np.arange(1,11)

print(f"array is , {nd1}")

# indexing
print(nd1[0],nd1[9])

# sliciing

print(nd1[3:-1:])

#2-d
"""

nd2[row_start:row_end,col_start:col_end]
"""
nd2=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"array is , {nd2}")

#indexing

print(nd2[0,2])

# slicing
print(nd2[1,:])

"""

"""
nd3=np.array([ [ [1,2,3],[4,5,6],[7,8,9] ],[ [13,14,15],[16,17,18],[19,20,21] ] ])

print(f"array is ",nd3)

# indexing

print(nd3[0,1,2])

# slicing
print(nd3[:,0:2,0:2])