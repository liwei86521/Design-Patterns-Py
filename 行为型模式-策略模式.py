# -*- coding:utf-8 -*-

"""
超市做活动，如果你的购物积分满1000，就可以按兑换现金抵用券10元，如果购买同一商品满10件，就可以打9折，
如果如果购买的金额超过500，就可以享受满减50元的优惠。这是三个不同的促销策略。
"""
from collections import namedtuple

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

class Order: #订单类  对应 Context
    def __init__(self, customer, promotion=None):
        self.cart = []
        self.customer = customer
        self.promotion = promotion

    def add_to_cart(self, *items):
        for item in items:
            self.cart.append(item)

    def total(self):
        total = 0
        for item in self.cart:
            total += item.total()

        return total

    def due(self): # 实际应付的钱
        if not self.promotion:
            discount = 0
        else:
            discount  = self.promotion.discount(self) # self 就是 order 对象
        return (self.total() - discount)

# 策略类，它是一个抽象基类
from abc import ABC, abstractmethod

class Promotion(ABC): # 促销抽象类  对应 Stragety
    @abstractmethod
    def discount(self, order): # 抽象方法
        pass

class FidelityPromo(Promotion): # 促销具体类的实现 1  ConcreteStragety
    #如果积分满1000分，就可以兑换10元现金券
    def discount(self, order): # fidelity  忠诚 积分
        return 10 if order.customer.fidelity >1000 else 0

class BulkItemPromo(Promotion): # 促销具体类的实现 2
    #如果单项商品购买10件，即可9折。
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 10:
                discount += item.total() * 0.1
        return discount

class LargeOrderPromo(Promotion): # 促销具体类的实现 3
    #如果订单总金额大于等于500，就可以立减50
    def discount(self, order):
        discount = 0
        if order.total() >= 500:
            discount = 50

        return discount

# 测试 各种 打折
def client_1():
    Customer = namedtuple('Customer', 'name fidelity')
    xm = Customer('小明', 1500)
    item1 = Item('纸巾', 20, 10)
    item2 = Item('食用油', 50, 4)
    item3 = Item('牛奶', 50, 4)

    order1 = Order(xm, FidelityPromo())
    order1.add_to_cart(item1, item2, item3)
    print(order1.total(), order1.due())  # 600 590

    order2 = Order(xm, BulkItemPromo())
    order2.add_to_cart(item1, item2, item3)
    print(order2.total(), order2.due()) # 600 580.0

    order3 = Order(xm, LargeOrderPromo())
    order3.add_to_cart(item1, item2, item3)
    print(order3.total(), order3.due())  # 600 550

# client_1()

# 良心的商家 能自动对比所有策略得出最优惠的价格来给到顾客。
#print(globals()) # 可以打印出 所以的 全局 类 和 全局方法
# 实现一个最优策略类
class BestPromo(Promotion):
    def discount(self, order):
        # 找出当前文件中所有的策略
        all_promotion = [globals()[name] for name in globals()  if name.endswith('Promo') and name != 'BestPromo']
        #print("all_promotion: ", all_promotion) # [<class '__main__.FidelityPromo'>, <class '__main__.BulkItemPromo'>, <class '__main__.LargeOrderPromo'>]

        # 计算最大折扣
        bestStragetyVal = max([promo().discount(order) for promo in all_promotion])
        bestStragety = [promo for promo in all_promotion if promo().discount(order) == bestStragetyVal]

        print("bestStragety ---> ", bestStragety) # bestStragety --->  [<class '__main__.LargeOrderPromo'>]
        return bestStragetyVal


def client_2():
    Customer = namedtuple('Customer', 'name fidelity')
    xm = Customer('小明', 1500)
    item1 = Item('纸巾', 20, 10)
    item2 = Item('食用油', 50, 4)
    item3 = Item('牛奶', 50, 4)

    order1 = Order(xm, BestPromo())
    order1.add_to_cart(item1, item2, item3)
    print(order1.total(), order1.due())  # 600 590

# client_2()
