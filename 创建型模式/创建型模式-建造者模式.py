# -*- coding:utf-8 -*-

#https://developer.aliyun.com/article/70416
#建造者模式的定义如下：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
#建造者模式的作用，就是将“构建”和“表示”分离，以达到解耦的作用。

#今天的例子，还是上一次谈到的快餐点餐系统。只不过，今天我们从订单的角度来构造这个系统

class Burger():
    name="" # 类对象  # 这里的 类对象 提供默认值
    price=0.0
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger" # 成员对象
        self.price=10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0

class Snack(): #小食
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0

class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

class Beverage(): # 饮料
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0

class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

#我们是要建造一个订单，因而，需要一个订单类。假设，一个订单，包括一份主食，一份小食，一种饮料。
class order():
    burger="" # 这里的 类对象 提供默认值
    snack=""
    beverage=""
    def __init__(self,orderBuilder):
        self.burger=orderBuilder.bBurger
        self.snack=orderBuilder.bSnack
        self.beverage=orderBuilder.bBeverage
    def show(self):
        print("Burger:%s"%self.burger.getName())
        print("Snack:%s"%self.snack.getName())
        print("Beverage:%s"%self.beverage.getName())

# 代码中的orderBuilder是什么鬼？这个orderBuilder就是建造者模式中所谓的“建造者”了
class orderBuilder():
    bBurger=""
    bSnack=""
    bBeverage=""
    def addBurger(self, xBurger):
        self.bBurger=xBurger  # 函数中的 成员变量
    def addSnack(self,xSnack):
        self.bSnack=xSnack
    def addBeverage(self,xBeverage):
        self.bBeverage=xBeverage

    def build(self): # ***
        return order(self)

def test1():
    order_builder = orderBuilder() # 初始化 建造者
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())

    order_1 = order_builder.build()
    order_1.show()

#在上面订单的构建过程中，如果将order直接通过参数定义好（其构建与表示没有分离），同时在多处进行订单生成，
# 此时需要修改订单内容，则需要一处处去修改，业务风险也就提高了不少。

#在建造者模式中，还可以加一个Director类，用以安排已有模块的构造步骤。
# 对于在建造者中有比较严格的顺序要求时，该类会有比较大的用处。
class orderDirector():
    order_builder=""
    def __init__(self,order_builder):
        self.order_builder=order_builder

    def createOrder(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()

def test2():
    order_builder = orderBuilder() # 初始化 建造者
    order_director= orderDirector(order_builder) # 初始化 orderDirector
    order_1 = order_director.createOrder(spicyChickenBurger(), chips(), coke())
    order_1.show()

if  __name__=="__main__":
    # test1()
    test2()