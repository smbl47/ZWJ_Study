class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "我的名字是{0},今年{1}岁".format(self.name, self.age)


stu = Student('小强',21)
print(dir(stu))
print(stu)
