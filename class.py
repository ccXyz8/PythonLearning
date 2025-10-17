class MyClass(object):

    args = 123

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print(self,flag=False):
        if flag:
            print(f"{self.name} is {self.age} years old {flag}")
        else:
            print(f"{self.name} is {self.age} years old")


ins = MyClass("ins","18")
ins.print(True)
print(ins.name)
ins.print()
print(MyClass.args is ins.args)
print(MyClass.args)
print(ins.args)
MyClass.args = 10000
print(MyClass.args)
print(ins.args)

