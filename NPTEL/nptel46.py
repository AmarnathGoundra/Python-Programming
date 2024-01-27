""" numpy basics """

import numpy as np

a=np.zeros((2,2))

b=np.ones((2,2))

c=np.full((2,2),6)

d=np.random.random((2,2))

x=np.array([[1,2],[3,4]], dtype= np.float64)

y=np.array([[5,6],[7,8]], dtype= np.float64)

e=np.array([1,2,3])
print(e.shape)

e=np.array([[1,2,3],[4,5,6]])
print(e.shape)

print(a)
print(b)
print(c)
print(d)
print(x)
print(y)

x=np.array([1,2])
print(x.dtype)
x=np.array([1.0,2.0])
print(x.dtype)

x=np.array([1,2], dtype=np.int64)
print(x.dtype)