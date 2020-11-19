# -*- coding:utf-8 -*-

#观察者模式也叫发布-订阅模式，定义：定义对象间一种一对多的依赖关系，使得当该对象状态改变时，
# 所有依赖于它的对象都会得到通知，并被自动更新。

class Observer:  # 观察者 基类
    def __init__(self, name):
        self.name = name

    def update(self):
        pass

class StockClerk(Observer):  # 具体观察者 看股票的职员
    def update(self, action):
        print(f"StockClerk {self.name} Got:  --> {action}")
        if action == "Boss Coming ...":
            self.close_stock_software()
        else:
            self.open_stock_software()

    def close_stock_software(self):
        print(f"{self.name} 关闭了股票软件，并开始 coding")

    def open_stock_software(self):
        print(f"{self.name} 又打开了股票软件，开始炒股")


class WatchNBAClerk(Observer):  # 具体观察者 看NBA的职员
    def update(self, action):
        print(f"WatchNBAClerk {self.name} Got:  --> {action}")
        if action == "Boss Coming ...":
            self.close_nba_software()
        else:
            self.open_nba_software()

    def close_nba_software(self):
        print(f"{self.name} 关闭了NBA软件, 打开了word开始写工作报告")

    def open_nba_software(self):
        print(f"{self.name} 又打开了NBA软件, 开始看NBA球赛")

class WatchTVClerk(Observer):  # 具体观察者 看TV的职员
    def update(self, action):
        print(f"WatchTVClerk {self.name} Got:  --> {action}")
        if action == "Boss Coming ...":
            self.close_tv_software()
        else:
            self.open_tv_software()

    def close_tv_software(self):
        print(f"{self.name} 关闭了TV软件, 打开了excel开始制表")

    def open_tv_software(self):
        print(f"{self.name} 又打开了TV软件, 开始看电视")


class Receptionist:  # 前台 Receptionist 被观察者（给各个观察者通风报信的人）
    observers = []  # 观察者列表，用来装观察者
    action = "" # 发现新的情况，比如：Boss来了

    def setAction(self, action):
        self.action = action

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyAll(self):
        for observer in self.observers:
            observer.update(self.action)

def client():
    c1 = StockClerk('John Wilson') # 实例化 观察者
    c2 = WatchNBAClerk('Herbert')
    c3 = WatchTVClerk("Dorra")

    # 被观察者 前台小姐姐 添加 观察者对象
    r = Receptionist()
    r.addObserver(c1)
    r.addObserver(c2)
    r.addObserver(c3)

    # 前台小姐姐 发现 boss 来了, 并通知所有观察者
    r.setAction("Boss Coming ...")
    r.notifyAll()

    print("--------------------------------------")
    # 前台小姐姐 发现 boss 走了, 并通知所有观察者
    r.setAction("Boss leaving ...")
    r.notifyAll()

client()
"""
StockClerk John Wilson Got:  --> Boss Coming ...
John Wilson 关闭了股票软件，并开始 coding
WatchNBAClerk Herbert Got:  --> Boss Coming ...
Herbert 关闭了NBA软件, 打开了word开始写工作报告
WatchTVClerk Dorra Got:  --> Boss Coming ...
Dorra 关闭了TV软件, 打开了excel开始制表
--------------------------------------
StockClerk John Wilson Got:  --> Boss leaving ...
John Wilson 又打开了股票软件，开始炒股
WatchNBAClerk Herbert Got:  --> Boss leaving ...
Herbert 又打开了NBA软件, 开始看NBA球赛
WatchTVClerk Dorra Got:  --> Boss leaving ...
Dorra 又打开了TV软件, 开始看电视

"""
