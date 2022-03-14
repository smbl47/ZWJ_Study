def fun1(a, b):
    c = a + b
    print(c)


# print(c)  # 超出函数作用域的范围


a = 100  # 全局变量


def fun2():
    print(a)


fun2()


def fun3():
    global b  # 函数内部定义的变量，局部变量使用global声明就变成了全局变量
    b = 200
    print(b)


fun3()
print(b)

