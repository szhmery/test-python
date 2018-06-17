# coding=utf8
import numpy as np

array = np.array([[1,2,3],[2,3,4]])
print('number of dimation:',array.ndim)
print('shape:',array.shape)
print('size:',array.size)

a = np.array([2,23,4],dtype=np.int)
print(a.dtype)
a = np.array([[2,23,4],[2,23,4]])
print(a)

a = np.zeros((3,4))
print(a)
a = np.ones((3,4),dtype=np.int16)
print(a)
a = np.empty((3,4))
print(a)
a= np.arange(10,20,2)
print(a)
a= np.arange(12).reshape((3,4))
print(a)
a= np.linspace(1,10,6).reshape((2,3))
print(a)