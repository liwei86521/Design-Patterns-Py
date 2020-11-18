# -*- coding:utf-8 -*-

"""
组合模式也叫作部分-整体模式，其定义如下：将对象组合成树形结构以表示“部分”和“整体”的层次结构，使得用户对单个对象和组合对象的使用具有一致性。
案例：公司结构组织
每一个公司都有自己的组织结构，越是大型的企业，其组织结构就会越复杂。大多数情况下，公司喜欢用“树形”结构来组织复杂的公司人事关系
和公司间的结构关系。一般情况下，根结点代表公司的最高行政权利单位，分支节点表示一个个部门，而叶子结点则会用来代表每一个员工。
每一个结点的子树，表示该结点代表的部门所管理的单位。假设一个具有HR部门，财务部门和研发部门，同时在全国有分支公司的总公司，
其公司结构，可以表示成如下逻辑：
"""

class Company:
    name = ""
    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        pass

    def listDuty(self):
        pass

class ConcreteCompany(Company): # 具体公司
    childrenCompany = None
    def __init__(self, name):
        Company.__init__(self,name)
        self.childrenCompany = []
    def add(self, company):
        self.childrenCompany.append(company)
    def remove(self, company):
        self.childrenCompany.remove(company)
    def display(self, depth):
        print('--'*depth + self.name)
        for component in self.childrenCompany:
            component.display(depth+1)
    def listDuty(self):
        for component in self.childrenCompany:
            component.listDuty()

class HRDepartment(Company):
    def __init__(self, name):
         Company.__init__(self,name)
    def display(self, depth):
        print ('--'*depth + self.name)
    def listDuty(self): #履行职责
        print ('%s\t Enrolling & Transfering management.' % self.name)

class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self,name)
    def display(self, depth):
        print ("--" * depth + self.name)
    def listDuty(self): #履行职责
        print ('%s\tFinance Management.'%self.name)

class RdDepartment(Company):
    def __init__(self,name):
        Company.__init__(self,name)
    def display(self, depth):
        print ("--"*depth+self.name)
    def listDuty(self):
        print ("%s\tResearch & Development."% self.name)

#在该例中，公司结构抽象仅考虑 公司（ConcreteCompany）和部门（Department），公司有子公司的可能性，公司也有自己的部门，部门是最终的叶子结点。
#假设总公司下设东边的分公司一个，东边的分公司下设东北公司和东南公司，显示公司层级，并罗列这些的公司中各部门的职责，可以构建如下业务场景：
def test():
    root = ConcreteCompany('HeadQuarter')
    root.add(HRDepartment('HQ HR'))
    root.add(FinanceDepartment('HQ Finance'))
    root.add(RdDepartment("HQ R&D"))

    comp = ConcreteCompany('East Branch')
    comp.add(HRDepartment('East.Br HR'))
    comp.add(FinanceDepartment('East.Br Finance'))
    comp.add(RdDepartment("East.Br R&D"))
    root.add(comp)

    comp1 = ConcreteCompany('Northast Branch')
    comp1.add(HRDepartment('Northeast.Br HR'))
    comp1.add(FinanceDepartment('Northeast.Br Finance'))
    comp1.add(RdDepartment("Northeast.Br R&D"))
    comp.add(comp1)

    comp2 = ConcreteCompany('Southeast Branch')
    comp2.add(HRDepartment('Southeast.Br HR'))
    comp2.add(FinanceDepartment('Southeast.Br Finance'))
    comp2.add(RdDepartment("Southeast.Br R&D"))
    comp.add(comp2)

    root.display(1)

    root.listDuty()

test()