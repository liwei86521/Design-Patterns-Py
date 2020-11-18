# -*- coding:utf-8 -*-
#https://zhuanlan.zhihu.com/p/57869247
#https://zhuanlan.zhihu.com/p/31675841
from abc import ABCMeta,abstractmethod
class Fruit(metaclass=ABCMeta): # 抽象方法定义
    @abstractmethod
    def getFruit(self): # 抽象方法
        raise AttributeError('子类必须实现这个方法')

class Banana(Fruit):
    def getFruit(self):  # 子类实现 抽象方法
        print("我是香蕉....")

class Apple(Fruit):
    def getFruit(self):  # 子类实现 抽象方法
        print("我是苹果....")


class Factory(object): # class
    def create(self, classname):
        dic = {"banana":Banana(), "apple":Apple()}
        return dic[classname].getFruit()

def Factory_Func(classname): # func
    dic = {"banana": Banana(), "apple": Apple()}
    return dic[classname].getFruit()

# Factory_Func("banana") # 我是香蕉....
# 工厂模式
fa = Factory()
fa.create("banana") # 传香蕉 就生产香蕉
fa.create("apple")

#######################################################################################

#抽象工厂、工厂方法异同比较：抽象工厂实例化的类在接口方法里已经通过字典方式例举出来了，
# 也就是不是实例化A就是B，但是抽象工厂实例化的类未知，可以在抽象接口类里传入A或者B
class AbsFactory(object): # 抽象工厂模式
    def __init__(self, classname): # 把类传进来
        self.classname = classname
    def create(self):
        self.classname().getFruit()

# 抽象工厂模式
af = AbsFactory(Apple) # 把类传进取 初始化
af.create()
af.classname = Banana
af.create()


