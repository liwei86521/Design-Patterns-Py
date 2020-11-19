# -*- coding:utf-8 -*-

#外包人员系统兼容:假设某公司A与某公司B需要合作，公司A需要访问公司B的人员信息，但公司A
# 与公司B协议接口不同，该如何处理？先将公司A和公司B针对各自的人员信息访问系统封装了对象接口。

class ACpnStaff:
    name=""
    id=""
    phone=""
    def __init__(self,id):
        self.id=id
    def getName(self):
        print("A protocol getName method...id:%s"%self.id)
        return self.name
    def setName(self,name):
        print("A protocol setName method...id:%s"%self.id)
        self.name=name
    def getPhone(self):
        print("A protocol getPhone method...id:%s"%self.id)
        return self.phone
    def setPhone(self,phone):
        print("A protocol setPhone method...id:%s"%self.id)
        self.phone=phone

class BCpnStaff:
    name=""
    id=""
    telephone=""
    def __init__(self,id):
        self.id=id
    def get_name(self):
        print("B protocol get_name method...id:%s"%self.id)
        return self.name
    def set_name(self,name):
        print("B protocol set_name method...id:%s"%self.id)
        self.name=name
    def get_telephone(self):
        print("B protocol get_telephone method...id:%s"%self.id)
        return self.telephone
    def set_telephone(self,telephone):
        print("B protocol get_name method...id:%s"%self.id)
        self.telephone=telephone

#为在A公司平台复用B公司接口，直接调用B公司人员接口是个办法，但会对现在业务流程造成不确定的风险。
# 为减少耦合，规避风险，我们需要一个帮手，就像是转换电器电压的适配器一样，
# 这个帮手就是协议和接口转换的适配器。适配器构造如下：

class CpnStaffAdapter:
    b_cpn=""
    def __init__(self,id):
        self.b_cpn=BCpnStaff(id)

    def getName(self):
        return self.b_cpn.get_name()
    def getPhone(self):
        return self.b_cpn.get_telephone()
    def setName(self,name):
        self.b_cpn.set_name(name)
    def setPhone(self,phone):
        self.b_cpn.set_telephone(phone)

class CpnStaffAdapter2(ACpnStaff):
    b_cpn = ""
    def __init__(self, XBCpnStaff):
        self.b_cpn = XBCpnStaff

    def getName(self): # 重写父类ACpnStaff 方法
        return self.b_cpn.get_name()

    def setName(self, name):
        self.b_cpn.set_name(name)

    def getPhone(self):
        return self.b_cpn.get_telephone()

    def setPhone(self, telephone):
        self.b_cpn.set_telephone(telephone)

#适配器将B公司人员接口封装，而对外接口形式与A公司人员接口一致，达到用A公司人员接口访问B公司人员信息的效果。
def test():
    acpn_staff = ACpnStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print("A Staff Name:%s" % acpn_staff.getName())
    print("A Staff Phone:%s" % acpn_staff.getPhone())

    bcpn_staff = CpnStaffAdapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print("B Staff Name:%s" % bcpn_staff.getName())
    print("B Staff Phone:%s" % bcpn_staff.getPhone())

#适配器将B公司人员接口封装，而对外接口形式与A公司人员接口一致，达到用A公司人员接口访问B公司人员信息的效果。
def test2():
    acpn_staff = ACpnStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print("A Staff Name:%s" % acpn_staff.getName())
    print("A Staff Phone:%s" % acpn_staff.getPhone())

    bcpn_staff = CpnStaffAdapter2(BCpnStaff("456"))
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print("B Staff Name:%s" % bcpn_staff.getName())
    print("B Staff Phone:%s" % bcpn_staff.getPhone())

test()
print("\n")
test2()