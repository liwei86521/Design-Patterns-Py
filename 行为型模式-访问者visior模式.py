# -*- coding:utf-8 -*-

"""
访问者模式 --> 数据类 与 数据的处理分离
数据类的处理方法我们叫它访问者，那么相同结构的数据面临不同的处理方式时，我们只需要创建不同的访问者
我们假设一种场景：上市公司的原始财务数据，对于会计来说需要制作各种报表，对于财务总监来说需要
分析公司业绩，对于战略顾问来说需要分析行业变化，我们来实现这一过程。
"""

class Finance:
    """财务数据结构类"""
    def __init__(self):
        self.salesvolume = None  # 销售额
        self.cost = None    # 成本
        self.history_salesvolume = None  # 历史销售额
        self.history_cost = None    # 历史成本

    def set_salesvolume(self, value):
        self.salesvolume = value

    def set_cost(self, value):
        self.cost = value

    def set_history_salesvolume(self, value):
        self.history_salesvolume = value

    def set_history_cost(self, value):
        self.history_cost = value

    def accept(self, visitor): # 接收各种 visitor 对财务数据进行分析
        pass

class Finance_year(Finance):
    """某一年的年财务数据类"""
    def __init__(self, year):
        Finance.__init__(self)
        self.visitors = []  # 分析师列表
        self.year = year

    def add_visitor(self, visitor): # 添加分析师
        self.visitors.append(visitor)

    def accept(self): #分析师列表里面的人去分析数据
        for obj in self.visitors:
            obj.visit(self) # 传入的参数self 为 Finance_year 对象

class Accounting: # 访问者 1
    """会计类"""
    def __init__(self):
        self.ID = "会计"
        self.Duty = "计算报表"

    def visit(self, finance_year_obj):
        print('会计年度： {}'.format(finance_year_obj.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        print('本年度纯利润： {}\n'.format(finance_year_obj.salesvolume - finance_year_obj.cost))

class Audit: # 访问者 2
    """财务总监类"""
    def __init__(self):
        self.ID = "财务总监"
        self.Duty = "分析业绩"

    def visit(self, finance_year_obj):
        print('会计总监年度： {}'.format(finance_year_obj.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if finance_year_obj.salesvolume - finance_year_obj.cost > finance_year_obj.history_salesvolume - finance_year_obj.history_cost:
            msg = "较同期上涨"
        else:
            msg = "较同期下跌"
        print('本年度公司业绩： {}\n'.format(msg))

class Advisor: # 访问者 3
    """战略顾问"""
    def __init__(self):
        self.ID = "战略顾问"
        self.Duty = "制定明年战略"

    def visit(self, finance_year_obj):
        print('战略顾问年度： {}'.format(finance_year_obj.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if finance_year_obj.salesvolume > finance_year_obj.history_salesvolume:
            msg = "行业上行，扩大生产规模"
        else:
            msg = "行业下行，减小生产规模"
        print('本年度公司业绩： {}\n'.format(msg))

class AnalyseData:
    """执行分析"""
    def __init__(self):
        self.datalist = []  # 需要处理的年度数据列表

    def add_data(self, year_data):
        self.datalist.append(year_data)

    def remove_data(self, year_data):
        self.datalist.remove(year_data)

    def analysis_all_year_data(self):
        for obj in self.datalist:
            obj.accept()
            print("******************************")

def client():
    finance_2018 = Finance_year(2018)  # 2018年的财务数据
    finance_2018.set_salesvolume(200)
    finance_2018.set_cost(90)
    finance_2018.set_history_salesvolume(190)
    finance_2018.set_history_cost(70)

    accounting = Accounting()
    audit = Audit()
    advisor = Advisor()  # 顾问

    finance_2018.add_visitor(accounting)  # 添加 visitor
    finance_2018.add_visitor(audit)  # 添加 visitor
    finance_2018.add_visitor(advisor)  # 添加 visitor

    finance_2018.accept() # 直接处理

# client()
"""
会计年度： 2018
我的身份是： 会计 职责： 计算报表
本年度纯利润： 110

会计总监年度： 2018
我的身份是： 财务总监 职责： 分析业绩
本年度公司业绩： 较同期下跌

战略顾问年度： 2018
我的身份是： 战略顾问 职责： 制定明年战略
本年度公司业绩： 行业上行，扩大生产规模
"""

def client2():
    w = AnalyseData()  # 计划安排会计，总监，顾问对2018年数据处理
    finance_2018 = Finance_year(2018)  # 2018年的财务数据
    finance_2018.set_salesvolume(200)
    finance_2018.set_cost(90)
    finance_2018.set_history_salesvolume(190)
    finance_2018.set_history_cost(70)

    accounting = Accounting()
    audit = Audit()
    advisor = Advisor() # 顾问

    finance_2018.add_visitor(accounting) # 添加 visitor
    finance_2018.add_visitor(audit) # 添加 visitor
    finance_2018.add_visitor(advisor) # 添加 visitor

    w.add_data(finance_2018)

# -------------------------------------------------------------

    finance_2020 = Finance_year(2020)  # 2018年的财务数据
    finance_2020.set_salesvolume(500)
    finance_2020.set_cost(180)
    finance_2020.set_history_salesvolume(400)
    finance_2020.set_history_cost(200)

    audit2 = Audit()
    advisor2 = Advisor() # 顾问

    finance_2020.add_visitor(audit2) # 添加 visitor
    finance_2020.add_visitor(advisor2) # 添加 visitor

    w.add_data(finance_2020)

    w.analysis_all_year_data()


client2()

