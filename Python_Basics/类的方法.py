# 定义一个类
class Student:
    stu_name = "小强"  # 直接写在类里面的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name称为实体属性，进行了一个赋值的操作，将局部变量name赋值给实体属性
        self.age = age

    # 实例方法
    def shili(self):
        print("你的名字")

    # 定义静态方法
    @staticmethod
    def jingtai():
        print("这是一个静态方法")

    # 定义类方法
    @classmethod
    def cl(cls):
        print("这是一个类方法")


# 在类外面定义的是函数，在里面的是方法
def outside():
    pass


# 创建类的对象
stu1 = Student("小强", 20)  # stu1就是实例对象,Student就是类
print("----------实例方法的使用方式-------------")
stu1.shili()  # 这两行的代码一样,第一行叫对象名.方法
Student.shili(stu1)  # 类名.方法名(类的对象)----->就是方法定义处的self
# print('-----------------------------------')
# print(stu1.name)
# print(stu1.age)

# 类属性的使用方式
print(Student.stu_name)
print(stu1.stu_name)

print("----------类方法的使用方式-------------")
Student.cl()
print("----------静态方法的使用方式-------------")
Student.jingtai()
