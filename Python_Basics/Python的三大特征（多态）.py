class Animal(object):
    def eat(self):
        print("动物要吃东西")


class Dog(Animal):
    def eat(self):
        print("狗吃肉")


class Cat(Animal):
    def eat(self):
        print("猫吃鱼")


class Preson(object):
    def eat(self):
        print("人吃五谷杂粮")


def fun(animal):
    animal.eat()


fun(Dog())
fun(Cat())
fun(Animal())
print('-----------------上方为继承关系--------------------')
print('-----------------下方不存在继承关系--------------------')
fun(Preson())
