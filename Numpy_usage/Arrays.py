import numpy as np

# a = np.array([1,2,3,4])
# print(type(a))
# print(a.shape)
# print(a.size)
# print(a[0],a[1],a[2],a[3])
# a[0]=5
# print(a)
#
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(type(b))
# print(b.shape)
# print(b.size)
# print(b[0],b[1],b[2])
# print(b[0,0],b[1,0],b[2,0])

a = np.zeros(5)
print(a)
print(type(a))
print(a.shape)

a = np.zeros((2,2))
print(a)
print(type(a))
print(a.shape)

a = np.ones((2,2))
print(a)
print(type(a))
print(a.shape)

a = np.full((2,2), 5)
print(a)
print(type(a))
print(a.shape)

a = np.eye(2)
print(a)
print(type(a))
print(a.shape)

a = np.random.random((2,2))
print(a)
print(type(a))
print(a.shape)
