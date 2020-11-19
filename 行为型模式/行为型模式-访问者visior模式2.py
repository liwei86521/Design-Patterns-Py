# -*- coding:utf-8 -*-

"""
访问者模式 --> 数据类 与 数据的处理分离
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
    def accept(self):
        pass

class Antibiotic(Medicine): #药品类中有两个子类，抗生素和感冒药
    def __init__(self,name,price):
        super().__init__(name,price) # 继承父类的 有参构造
        self.visitors = []  # visitor 列表

    def add_visitor(self, visitor): # 添加visitor 如 划价员和药房管理员
        self.visitors.append(visitor)

    def accept(self):
        for obj in self.visitors:
            obj.visit(self)

class Coldrex(Medicine):
    def __init__(self,name,price):
        super().__init__(name,price) # 继承父类的 有参构造
        self.visitors = []  # visitor 列表

    def add_visitor(self, visitor):  # 添加visitor 如 划价员和药房管理员
        self.visitors.append(visitor)

    def accept(self):
        for obj in self.visitors:
            obj.visit(self) # 这里的 self 为 Coldrex 对象


class Visitor:
    name=""
    def setName(self,name):
        self.name=name
    def visit(self,medicine):
        pass
class Charger(Visitor):
    def visit(self,medicine_obj):
        print ("CHARGE: %s lists the Medicine %s. Price:%s " % (self.name, medicine_obj.getName(), medicine_obj.getPrice()))
class Pharmacy(Visitor):
    def visit(self,medicine_obj):
        print ("PHARMACY:%s offers the Medicine %s. Price:%s" % (self.name, medicine_obj.getName(), medicine_obj.getPrice()))

#工作人员分为划价员和药房管理员。
#在药品类中，有一个add_visitor 可以添加visitor， 有一个accept方法，表示不同的visitor对 同一种Medicine进行不同的处理，
# 所有的 Visitor 类中都包含一个 visit方法，参数又恰是Medicine 对象，药品作为处理元素，依次允许Visitors对其进行操作

#药方类的构建, 药方类将待处理药品进行整理，并组织Visitors依次处理
class ObjectStructure:
    pass
class Prescription(ObjectStructure): #Prescription  处方
    medicines=[]
    def addMedicine(self,medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self,medicine):
        self.medicines.append(medicine)

    def analysis_all_medicines(self):
        for medc in self.medicines:
            medc.accept()
            print("-----------------------------")

def client(): #业务代码
    yinqiao_pill = Coldrex("Yinqiao Pill", 2.0)
    penicillin = Antibiotic("Penicillin", 3.0)

    charger = Charger()  # 划价员
    charger.setName("Doctor Strange")
    pharmacy = Pharmacy()  # 药房管理员
    pharmacy.setName("Doctor Wei")

    yinqiao_pill.add_visitor(charger)
    yinqiao_pill.add_visitor(pharmacy)

    penicillin.add_visitor(charger)
    penicillin.add_visitor(pharmacy)

    doctor_prsrp = Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)

    doctor_prsrp.analysis_all_medicines()

client()
