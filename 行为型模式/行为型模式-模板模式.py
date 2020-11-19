# -*- coding:utf-8 -*-
import abc
#员工基类相当于一个员工模版，定义了一个员工的通用行为
class Employee():
    def __init__(self, name):
        self.name = name

    def clock_in(self):
        print(f"{self.name} 打卡上班")

    @abc.abstractmethod
    def work(self): # 抽象方法
        pass

    def noon_break(self):
        print(f"{self.name} 正在午休")

    def clock_out(self):
        print(f"{self.name} 打卡下班")

    def daily_work(self):
        self.clock_in()
        self.work()
        self.noon_break()
        self.work()
        self.clock_out()

#具体员工继承员工基类，定义了属于自己的特定行为
class Programmer(Employee):
    def work(self):
        print(f"{self.name} 正在coding...")


class Manager(Employee):
    def work(self):
        print(f"{self.name} 正在meeting...")


def client():
    p = Programmer("snow")
    p.daily_work()

    m = Manager("boss")
    m.daily_work()

# client()
