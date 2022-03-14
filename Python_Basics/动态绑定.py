class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shili(self):
        print(self.name + "正在工作！")


stu1 = Student('小强', 20)
stu2 = Student('小帅', 21)
print(stu1.name)
print("--------给类动态绑定属性----------")
stu1.gender = "男"
print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)
print("--------给类动态绑定方法----------")
# 原方法
stu1.shili()
stu2.shili()


def show():
    print("定义在类之外的是函数")


stu1.show = show
stu1.show()
