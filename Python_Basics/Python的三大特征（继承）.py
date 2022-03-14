class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    # 方法重写
    def info(self):
        # super().info()  # 调用父类中被重写的方法
        print(self.name, self.age, self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, tech_no):
        super().__init__(name, age)
        self.tech_no = tech_no


stu = Student('张三', 20, '1001')
teacher = Teacher('李四', 32, 10)

stu.info()
teacher.info()


# 多继承类

class A(object):
    pass


class B(object):
    pass


class C(A, B):
    pass
