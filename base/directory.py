direct = {"abc":1,"def":2,"ghi":3}
print(direct)
print(direct.popitem())
print(direct.fromkeys([i for i in range(6)],))
direct.update({"abc":4,"def":5})
print(direct)