# -*- coding:utf-8 -*-

"""
访问者模式的定义：封装一些作用于某种数据结构中的各元素的操作，它可以在不改变数据结构的前提下定义于作用于这些元素的新操作。
案例：药房业务系统
假设一个药房，有一些大夫，一个药品划价员和一个药房管理员，它们通过一个药房管理系统组织工作流程。大夫开出药方后，
药品划价员确定药品是否正常，价格是否正确；通过后药房管理员进行开药处理。该系统可以如何实现？最简单的想法，
是分别用一个一个if…else…把划价员处理流程和药房管理流程实现，这样做的问题在于，扩展性不强，而且单一性不强，
一旦有新药的加入或者划价流程、开药流程有些变动，会牵扯比较多的改动。今天介绍一种解决这类问题的模式：访问者模式。
首先，构造药品类和工作人员类：
"""
class Medicine:
    name=""
    price=0.0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def accept(self,visitor):
        pass
class Antibiotic(Medicine): #药品类中有两个子类，抗生素和感冒药
    def accept(self,visitor):
        visitor.visit(self)
class Coldrex(Medicine):
    def accept(self,visitor):
        visitor.visit(self)


class Visitor:
    name=""
    def setName(self,name):
        self.name=name
    def visit(self,medicine):
        pass
class Charger(Visitor):
    def visit(self,medicine):
        print ("CHARGE: %s lists the Medicine %s. Price:%s " % (self.name, medicine.getName(), medicine.getPrice()))
class Pharmacy(Visitor):
    def visit(self,medicine):
        print ("PHARMACY:%s offers the Medicine %s. Price:%s" % (self.name, medicine.getName(), medicine.getPrice()))

#工作人员分为划价员和药房管理员。
#在药品类中，有一个accept方法，其参数是个visitor；而工作人员就是从Visitor类中继承而来的，也就是说，他们就是Visitor，
# 都包含一个visit方法，其参数又恰是medicine。药品作为处理元素，依次允许（Accept）Visitor对其进行操作

#药方类的构建, 药方类将待处理药品进行整理，并组织Visitor依次处理
class ObjectStructure:
    pass
class Prescription(ObjectStructure): #Prescription  处方
    medicines=[]
    def addMedicine(self,medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self,medicine):
        self.medicines.append(medicine)
    def visit(self,visitor):
        for medc in self.medicines:
            medc.accept(visitor)

def test(): #业务代码
    yinqiao_pill = Coldrex("Yinqiao Pill", 2.0)
    penicillin = Antibiotic("Penicillin", 3.0)
    doctor_prsrp = Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)

    charger = Charger() # 划价员
    charger.setName("Doctor Strange")
    pharmacy = Pharmacy() # 药房管理员
    pharmacy.setName("Doctor Wei")
    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharmacy)

test()