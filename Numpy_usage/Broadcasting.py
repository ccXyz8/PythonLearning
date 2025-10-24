import numpy as np

# x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# v = np.array([1,0,1])
# y = np.empty_like(x)
#
# # for i in range(4):
# #     y[i,:] = x[i,:]+v
# #
# # print(y)
# #
# # vv = np.tile(v,(4,1))
# # print(vv)
# # y = x+vv
# # print(y)
#
# y = x+v
# print(y)


v = np.array([[1,2,3]])
w = np.array([4,5])
print(np.reshape(v,(3,1))*w)


x = np.array([[1,2,3],
              [4,5,6]])

print(x+v)

print((x.T+w).T)

print(x+np.reshape(w,(2,1)))

print(x*2)
