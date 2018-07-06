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

## section 5
a = np.array([10,20,30,40])
b = np.arange(4)
print(a,b)
c = a - b
print(c)
c = a + b
print(c)
c = b**2
print(c)
c = 10*np.sin(a)
print(c)
print(b<3)
print(b==3)

a=np.array([[1,1],[0,1]])
b = np.arange(4).reshape((2,2))
print(a)
print(b)
c=a*b
print(c)
c_dot = np.dot(a,b)
print(c_dot)
c_dot_2 = a.dot(b)
print(c_dot_2)

a = np.random.random((2,4))
print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))

print(np.sum(a,axis=1))
print(np.min(a,axis=0))
print(np.max(a,axis=1))

##section 6
A=np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A))
print(np.argmax(A))

print(np.mean(A))
print(A.mean())
print(np.average(A))
print(np.median(A))
print(np.cumsum(A))
print(np.diff(A))
print(np.nonzero(A))

A = np.arange(14,2,-1).reshape((3,4))
print(A)
print(np.transpose(A))
print(A.T)
print(A.T.dot(A))
print(np.clip(A,5,9))
print(np.mean(A,axis=1))

##section 7
A = np.arange(3,15)
print(A)
print(A[3])
A=A.reshape((3,4))
print(A)
print(A[2])
print(A[2][1])
print(A[2,1])
print(A[:,1])
print(A[1,1:3])
for row in A:
    print(row)
for column in A.T:
    print(column)
A = np.arange(3,15).reshape((3,4))
print(A.flatten())
for item in A.flat:
    print(item)