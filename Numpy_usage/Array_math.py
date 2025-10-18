import numpy as np

# x = np.array([[1,2],[3,4]],dtype=np.float64)
# y = np.array([[5,6],[7,8]],dtype=np.float64)

# print(x+y)
# print(np.add(x,y))
#
# print(x-y)
# print(np.subtract(x,y))
#
# print(x*y)
# print(np.multiply(x,y))
#
# print(x/y)
# print(np.divide(x,y))
#
# print(np.sqrt(x))

# v = np.array([9,10])
# w = np.array([11,12])
#
# print(v.dot(w))
# print(np.dot(v,w))

#这是2*2 x 1*2 就是数乘 结果也是1*2
# print(x.dot(v))
# print(np.dot(x,v))

#这次是1*2 x 2*2 就是矩阵乘法 结果自然是1*2
# print(v.dot(x))
# print(np.dot(v,x))

# print(x.dot(y))
# print(np.dot(x,y))

x = np.array([[1,2],[3,4]])
print(x)
print(x.shape)
print(x.T)
print(x.T.shape)

y = np.array([1,2,1])
print(y)
print(y.shape)
print(y.T)
print(y.T.shape)