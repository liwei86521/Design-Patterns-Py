# -*- coding:utf-8 -*-

"""
假设某司维护着一些客户资料，需要在该司有新产品上市或者举行新活动时通知客户。现通知客户的方式有两种：
短信通知、邮件通知。应如何设计该系统的客户通知部分？为解决该问题，我们先构造客户类，
包括客户常用的联系方式和基本信息，同时也包括要发送的内容。
"""
class customer:
    customer_name=""
    snd_way=""
    info=""
    phone=""
    email=""

    def setPhone(self,phone):
        self.phone=phone
    def setEmail(self,mail):
        self.email=mail
    def setInfo(self,info):
        self.info=info
    def setName(self,name):
        self.customer_name=name
    def setBrdWay(self,snd_way):
        self.snd_way=snd_way

    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email

    def sndMsg(self):
        self.snd_way.send(self.info)

#snd_way向客户发送信息的方式，该方式置为可设，即可根据业务来进行策略的选择。发送方式构建如下：
class msgSender:
    dst_code=""
    def setCode(self,code):
        self.dst_code=code
    def send(self,info):
        pass
class emailSender(msgSender): # 邮件通知
    def send(self,info):
        print("EMAIL_ADDRESS:%s  INFO:%s"%(self.dst_code,info))

class textSender(msgSender): # 短信通知
    def send(self,info):
        print("TEXT_CODE:%s  INFO:%s"%(self.dst_code,info))

#在业务场景中将发送方式作为策略，根据需求进行发送。
def test():
    customer_x = customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")
    customer_x.setEmail("customer_x@xmail.com")
    customer_x.setInfo("Welcome to our new party!")

    text_sender = textSender()
    text_sender.setCode(customer_x.getPhone())
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()

    mail_sender = emailSender()
    mail_sender.setCode(customer_x.getEmail())
    customer_x.setBrdWay(mail_sender)
    customer_x.sndMsg()

#以上述例子为例，customer类扮演的角色 直接依赖抽象策略的接口，在具体策略实现类中即可定义个性化的策略方式，且可以方便替换。
test()