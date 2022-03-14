# 默认值参数
def fun(a, b=50):
    print(a, b)


fun(10)
fun(10, 100)
print("--------------------------------")


# 个数可变的位置参数
def fun1(*args):
    print(args)


fun1(10)
fun1(20, 30)
fun1(40, 50, 60)


# 个数可变的关键字参数
def fun2(**kwargs):
    print(kwargs)


fun2(a=10)

print("--------------------------------")


# 函数的位置参数

def fun3(a, b, c):
    print("a=", a, "b=", b, "c=", c)


lists = (11, 22, 33)
fun3(10, 20, 30)
fun3(*lists)  # '''如果是位置参数，在函数调用时，将列表的每个元素都转换为位置参数传入'''

print("--------------------------------")


# 函数的关键字参数
def fun4(a=100, b=200, c=300):
    print("a=", a, "b=", b, "c=", c)


dico = {"a": 111, "b": 222, "c": 333}
fun4(**dico)  # '''如果是关键字参数，在函数调用时，将字典的每个元素都转换为关键字参数传入'''
print("--------------------------------")


# 函数的位置与关键字参数的传递
def fun5(a, *, b, c, d):  # *表示在*之后的参数只能使用关键字参数传递
    print("a=", a, "b=", b, "c=", c, "d=", d)


fun5(10, 20, 30, 40)
fun5(a=10, b=20, c=30, d=40)


# 函数定义时形参的顺序问题
def fun6(a, b, *, c, d, **kwargs):
    pass


def fun7(*args, **kwargs):
    pass


def fun8(a, b=10, *args, **kwargs):
    pass
