# -*- coding:utf-8 -*-

#观察者模式也叫发布-订阅模式，定义：定义对象间一种一对多的依赖关系，使得当该对象状态改变时，所有依赖于它的对象都会得到通知，并被自动更新。

#我们将从业务流程的实现角度，来再次实现该火警报警器。
#三个传感器类:报警器、洒水器、拨号器都是“观察”烟雾传感器的情况来做反应的。因而，他们三个都是观察者，
# 而烟雾传感器则是被观察对象了。根据分析，将三个类提取共性，泛化出“观察者”类，并构造被观察者。
class AlarmSensor:
    def run(self):
        print ("Alarm Ring...")
class WaterSprinker:
    def run(self):
        print ("Spray Water...")
class EmergencyDialer:
    def run(self):
        print ("Dial 119...")

#观察者如下
class Observer:
    def update(self):
        pass
class AlarmSensor(Observer):
    def update(self,action):
        print ("Alarm Got: %s" % action)
        self.runAlarm()
    def runAlarm(self):
        print ("Alarm Ring...")
class WaterSprinker(Observer):
    def update(self,action):
        print("Sprinker Got: %s" % action)
        self.runSprinker()
    def runSprinker(self):
        print ("Spray Water...")
class EmergencyDialer(Observer):
    def update(self,action):
        print ("Dialer Got: %s"%action)
        self.runDialer()
    def runDialer(self):
        print ("Dial 119...")

#观察者中定义了update接口，如果被观察者状态比较多，或者每个具体的观察者方法比较多，
# 可以通过update传参数进行更丰富的控制。
#下面构造被观察者
class Observed:
    observers=[] # 观察者列表，用来装观察者
    action=""
    def addObserver(self,observer):
        self.observers.append(observer)
    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)

class smokeSensor(Observed):
    def setAction(self,action):
        self.action=action
    def isFire(self):
        return True

#被观察者中首先将观察对象加入到观察者数组中，若发生情况，则通过notifyAll通知各观察者。

def test(): #业务代码
    alarm = AlarmSensor()
    sprinker = WaterSprinker()
    dialer = EmergencyDialer()

    smoke_sensor = smokeSensor()
    smoke_sensor.addObserver(alarm) # 被观察者 添加 观察者
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)

    if smoke_sensor.isFire():
        smoke_sensor.setAction("On Fire!")
        smoke_sensor.notifyAll()

test()