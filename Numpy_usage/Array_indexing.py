import numpy as np

# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# b = a[:2,1:3]
# print(b.shape)
# print(type(b))
# print(b)

# b = a[1:3,1:3]
# print(b.shape)
# print(type(b))
# print(b)

# print(a[0,1])
# b[0,0]=77
# print(a[0,1])

# r1 = a[1,:]
# r2 = a[1:2,:]
# print(r1,r1.shape)
# print(r2,r2.shape)
#
# r1[0]=100
# print(r1)
# print(a[1,:])
# r2[0][0]=101
# print(r2)
# print(a[1:2,:])

# r1 = a[:,1]
# r2 = a[:,1:2]
# print(r1,r1.shape)
# print(r2,r2.shape)

# a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# print(a[[0,1,2],[0,1,0]])
# print(np.array(a[[0,1,2],[0,1,0]]))
#
# print(a[[0,0],[1,1]])
# print(np.array(a[[0,0],[1,1]]))

# print(a)
# b = np.array([0,2,0,1])
# print(a[np.arange(4),b])
#
# a[np.arange(4),b]+=10
# print(a)

a = np.array([[1,2],[3,4],[5,6]])

bool_idx = (a>2)
print(bool_idx)

print(a[bool_idx])

print(a[a>2])
