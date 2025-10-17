# import this
import copy
import math
import random

# list = [1,2,3,4,]
#
# list.append(5)
# print(list)

# list = [1,3,4,2,1]
# print(list)
# print(sorted(list,reverse=True))
# list.sort()
# print(list)

# list = list(range(6))
# print(list)
# print(list[:-1])
# print(list[-2:-1])
# print(list[0:-1])
# print(list[-len(list)+1:])

# list = list(range(10))
# print(list)
# copy_list = list.copy()
# copy2_list = list[:]
# copy3_list = list
# print(copy_list)
#
# list[0]=1
# print(list)
# print(copy_list)
# print(copy2_list)
# print(copy3_list)


list = list(range(6))
# random.shuffle(list)
# print(list)
# print(random.random())
#
# print(math.exp(random.random()))

def modify(list):
    inner_list = copy.deepcopy(list)
    for index in range(len(inner_list)):
        inner_list[index]+=1
    return inner_list

print(list)
print(modify(list))
print(list)

