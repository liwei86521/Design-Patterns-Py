# -*- coding:utf-8 -*-
import threading
import time
#https://zhuanlan.zhihu.com/p/31675841
#单例模式是指：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
# 实现__new__方法, 比__init__更早执行,并在将一个类的实例绑定到类变量_instance上
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton): # 继承
    a = 1

one = MyClass()
two = MyClass()
print(id(one) == id(two)) # True  --- > 单例模式

#总线是计算机各种功能部件或者设备之间传送数据、控制信号等信息的公共通信解决方案之一。
# 现假设有如下场景：某中央处理器（CPU）通过某种协议总线与一个信号灯相连，信号灯有64种颜色可以设置，
# 中央处理器上运行着三个线程，都可以对这个信号灯进行控制，并且可以独立设置该信号灯的颜色。
# 抽象掉协议细节（用打印表示），如何实现线程对信号等的控制逻辑。


#总线
class Bus(Singleton):
    lock = threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(1) # 模拟真正的逻辑处理
        print("Sending Signal Data...", data)
        self.lock.release()

#线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus="" # 类变量
    name=""
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)

if  __name__=="__main__":
    for i in range(10):
        print("Entity %d begin to run..."%i)
        my_entity=VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()

