# -*- coding:utf-8 -*-

"""
命令模式的几个核心角色及其分工：
    Receiver（命令的内容）：接收者，具体执行动作的对象
    Command（命令基类）：主要声明抽象命令类的接口
    ConcreteCommand（命令实现）：复写基类中声明的接口，实现具体的调用功能
    Invoker(命令调度和执行)：全部命令的执行和调度入口
    Client（命令装配者）:创建具体的命令对象，组装命令对象和接收者
"""

class Receiver(object):
    """具体动作"""
    def __init__(self, word):
        self.word = word

    def run(self):
        print(self.word)

class Command(object):
    """声明命令模式接口"""
    def __init__(self, obj): # 接收 Receiver obj
        self.obj = obj

    def execute(self):
        pass

class ConcreteCommand(Command):
    """实现命令模式接口"""
    def execute(self):
        self.obj.run()

class Invoker(object):
    """接受命令并执行命令的接口"""
    def __init__(self):
        self._commands = []

    def add_command(self, cmd):
        self._commands.append(cmd)

    def remove_command(self, cmd):
        self._commands.remove(cmd)

    def run_command(self):
        for cmd in self._commands:
            cmd.execute()

def client():
    """装配者"""
    invoker = Invoker()
    cmd1 = ConcreteCommand(Receiver('命令一'))
    invoker.add_command(cmd1)
    cmd2 = ConcreteCommand(Receiver('命令二'))
    invoker.add_command(cmd2)
    cmd3 = ConcreteCommand(Receiver('命令三'))
    invoker.add_command(cmd3)
    invoker.run_command()

client()
"""
命令一
命令二
命令三
"""
