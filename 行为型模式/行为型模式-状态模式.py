# -*- coding:utf-8 -*-

"""
当控制一个对象的状态转换的条件表达式过于复杂时,把状态的判断逻辑转移到
表示不同状态的一系列类当中,可以把复杂的判断逻辑简化
"""

#先实现抽象的状态类：
class State(object):
    def __init__(self):
        pass

    def coding(self, w): # 写代码
        pass

class ForenoonState(State):
    def coding(self, w): # w 对应的是 一个对象 eg: Context()
        if w.hour < 12:
            print(f"当前时间: {w.hour} 点, 精神百倍")
        else:
            w.setState(AfternoonState())
            w.coding()

class AfternoonState(State):
    def coding(self, w):
        if w.hour < 17:
            print(f"当前时间: {w.hour}点, 状态还行,继续努力")
        else:
            w.setState(EveningState())
            w.coding()

class EveningState(State):
    def coding(self, w):
        if w.hour < 21:
            print(f"当前时间: {w.hour}点, 加班呢,疲劳了")
        else:
            w.setState(SleepState())
            w.coding()

class SleepState(State):
    def coding(self, w):
        print(f"当前时间: {w.hour}点, 不行了,睡着了")

#为在业务中调度状态转移，还需要将上下文进行记录，需要一个上下文的类。
class Context(object):
    currState=""
    def __init__(self):
        self.hour = 9
        self.currState = ForenoonState()

    def setState(self, currState):
        self.currState = currState

    def coding(self):
        self.currState.coding(self) # ps coding(self) 里面的 self 一定不能省略


def client():
    ctx = Context() # 初始状态为 ForenoonState
    ctx.coding()

    ctx.hour = 15
    ctx.coding()

    ctx.hour = 20
    ctx.coding()

    ctx.hour = 22
    ctx.coding()

client()

"""
当前时间: 9 点, 精神百倍
当前时间: 15点, 状态还行,继续努力
当前时间: 20点, 加班呢,疲劳了
当前时间: 22点, 不行了,睡着了
"""
