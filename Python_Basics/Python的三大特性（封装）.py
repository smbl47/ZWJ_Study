class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外面使用age
print(stu.name)
# print(stu.__age)   # 无法获取数据
# 强行访问
print(dir(stu))  # 返回当前范围内的变量、方法和定义的类型列表
print(stu._Student__age)
