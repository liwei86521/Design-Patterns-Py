# -*- coding:utf-8 -*-
#代理模式定义如下：为某对象提供一个代理，以控制对此对象的访问和控制。代理模式在使用过程中，应尽量对抽象主题类进行代理

# 代理模式实例: 网络服务器配置白名单
# https://zhuanlan.zhihu.com/p/92051694

class NotFindError(Exception): # 异常类
    def __init__(self, msg):
        self.msg = msg

class RealSubject(object): # 真实主题类
    def __init__(self):
        self.score = {
            "张三": 90,
            "李四": 59,
            "王二": 61
        }

    def num_students(self):
        num = len(self.score.keys())
        print(f"The number of students is {num}")

    def get_score(self, user_name):
        _score = self.score.get(user_name)
        print(f"The score of {user_name} is {_score}")

#代理模式的作用:当我们访问一个实体(真实主题)考虑到安全等因素不方便时，
# 代理可以为这个实体提供一个替代者，来控制它的访问权限和访问内容。
class Proxy(object):
    # def __init__(self, realSubject):
    #     self.default_passwd = "123"
    #     self.real_subject = realSubject

    def __init__(self):
        self.default_passwd = "123"
        self.real_subject = RealSubject() # 代理中有真实主题的对象

    def num_students(self):
        self.real_subject.num_students()

    def get_score(self, user_name):
        print("You are visiting {} score ...".format(user_name))
        passwd = input("Please input password : ")
        if passwd == self.default_passwd:
            if user_name in self.real_subject.score.keys():
                return self.real_subject.get_score(user_name)
            else:
                raise NotFindError("The student you are visiting not found.")
        else:
            raise ValueError("The password you provided is wrong!")

# client 端不能 直接与 真实主题连接
def client():
    #realSubject = RealSubject() # 真实主题类
    #proxy = Proxy(realSubject) # 代理类

    proxy = Proxy()
    proxy.num_students()
    proxy.get_score("张三")

client()
