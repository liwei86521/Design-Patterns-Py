# -*- coding:utf-8 -*-
"""案例：请假系统

假设有这么一个请假系统：员工若想要请3天以内（包括3天的假），只需要直属经理批准就可以了；如果想请3-7天，不仅需要直属经理批准，
部门经理需要最终批准；如果请假大于7天，不光要前两个经理批准，也需要总经理最终批准。类似的系统相信大家都遇到过，那么该如何实现呢？
首先想到的当然是if…else…，但一旦遇到需求变动，其臃肿的代码和复杂的耦合缺点都显现出来。简单分析下需求，“假条”在三个经理间是单向传递关系，
像一条链条一样，因而，我们可以用一条“链”把他们进行有序连接。
构造抽象经理类和各个层级的经理类："""
class manager():
    successor = None # 表示有没有更高一级的领导
    name = ""

    def __init__(self, name):
        self.name = name

    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request): # 定义为抽象接口
        pass

class lineManager(manager): #直属经理
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 3:
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)

class departmentManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 7:
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)
class generalManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff':
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))

class request(): # 请求封装
    requestType = ''
    requestContent = ''
    number = 0 # 请假天数

#request类封装了假期请求。在具体的经理类中，可以通过setSuccessor接口来构建“责任链”，并在handleRequest接口中实现逻辑。
def test():#场景类中实现
    line_manager = lineManager('LINE MANAGER')
    department_manager = departmentManager('DEPARTMENT MANAGER')
    general_manager = generalManager('GENERAL MANAGER')

    line_manager.setSuccessor(department_manager)
    department_manager.setSuccessor(general_manager)

    req = request()
    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 1 day off'
    req.number = 1
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 5 days off'
    req.number = 5
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 10 days off'
    req.number = 10
    line_manager.handleRequest(req)

test()