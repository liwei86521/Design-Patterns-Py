# -*- coding:utf-8 -*-

#桥接模式(Bridge Pattern):将抽象部分与它的实现部分分离，使它们都可以独立地变化
#程序实例:技能分类 和 人的分类 耦合度低 两种分类中间用一个set_skill桥接,可以实现调用不同的类，达到了解耦合的目的

# 功能类：技能
class Skill(object):
    def have_skill(self):
        pass

class S_code(Skill): # 具体功能类：编程
    def have_skill(self):
        print('我拥有编程技能！')

class S_teach(Skill): # 具体功能类：上课
    def have_skill(self):
        print('我拥有教书技能！')

class S_swim(Skill): #具体功能类： 游泳
    def have_skill(self):
        print('我拥有游泳技能！')

#抽象类：人
class Human(object):
    skill = ""
    def set_skill(self, skill):
        self.skill = skill

    def perform_skill(self):
        pass

# 具体抽象类：码农
class Programmer(Human):
    def perform_skill(self):  # 重写基类中的技能
        print('我是码农，给我力量吧！')
        self.skill.have_skill()

# 具体抽象类：老师
class Teacher(Human):
    def perform_skill(self):  # 重写基类中的技能
        print('我是教师，给我力量吧！')
        self.skill.have_skill()

def client():
    skill_1 = S_code()  # 编程技能
    skill_2 = S_teach()  # 教书技能
    skill_3 = S_swim()  # 游泳技能

    p = Programmer()  # 程序员
    p.set_skill(skill_1)  # 赋予程序员编程技能
    p.perform_skill()  # 演示这个技能
    p.set_skill(skill_2)  # 赋予程序员教书技能
    p.perform_skill()  # 演示教书技能

    print("----------------------------------------")

    t = Teacher()  # 教师
    t.set_skill(skill_2)  # 赋予教师教书技能
    t.perform_skill()  # 演示这个技能
    t.set_skill(skill_3)  # 赋予教师游泳技能
    t.perform_skill()  # 演示教书技能

client()
