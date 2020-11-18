# -*- coding:utf-8 -*-
#https://developer.aliyun.com/article/70417
#https://zhuanlan.zhihu.com/p/31675841

"""
快餐点餐系统:
想必大家一定见过类似于麦当劳自助点餐台一类的点餐系统吧。在一个大的触摸显示屏上，有三类可以选择的上餐品：
汉堡等主餐、小食、饮料。当我们选择好自己需要的食物，支付完成后，订单就生成了。
下面，我们用今天的主角--工厂模式--来生成这些食物的逻辑主体。
"""

#首先，来看主餐的生成（仅以两种汉堡为例）
class Burger():
    name=""
    price=0.0
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0


#其次，是小食。（内容基本一致）
class Snack():
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

#最后，是饮料
class Beverage():
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

#以上的Burger，Snack，Beverage，都可以认为是该快餐店的产品，由于只提供了抽象方法，我们把它们叫抽象产品类，
# 而cheeseBurger等6个由抽象产品类衍生出的子类，叫作具体产品类。接下来，“工厂”就要出现了。
class foodFactory():
    type=""
    def createFood(self,foodClass):
        print(self.type," factory produce a instance.")
        foodIns=foodClass()
        return foodIns

class burgerFactory(foodFactory):
    def __init__(self):
        self.type="BURGER"
class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"
class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"

#同样，foodFactory为抽象的工厂类，而burgerFactory，snackFactory，beverageFactory为具体的工厂类。
#在业务场景中，工厂模式是如何“生产”产品的呢

def test():
    burger_factory = burgerFactory()
    snack_factorry = snackFactory()
    beverage_factory = beverageFactory()

    cheese_burger = burger_factory.createFood(cheeseBurger)
    print(cheese_burger.getName(), cheese_burger.getPrice())

    chicken_wings = snack_factorry.createFood(chickenWings)
    print(chicken_wings.getName(), chicken_wings.getPrice())

    coke_drink = beverage_factory.createFood(coke)
    print(coke_drink.getName(), coke_drink.getPrice())

test()