# -*- coding:utf-8 -*-

"""
案例：电梯控制器
电梯在我们周边随处可见，电梯的控制逻辑中心是由电梯控制器实现的。电梯的控制逻辑，即使简单点设计，把状态分成开门状态，
停止状态和运行状态，操作分成开门、关门、运行、停止，那流程也是很复杂的。首先，开门状态不能开门、运行、停止；
停止状态不能关门，停止；运行状态不能开门、关门、运行。要用一个一个if…else…实现，首先代码混乱，不易维护；二是不易扩展。
那该如何实现？在上边的逻辑中，每个操作仅仅是一个操作，状态切换与操作是分离的，这也造成后来操作和状态“相互配合”的“手忙脚乱”。
如果把状态抽象成一个类，每个状态为一个子类，每个状态实现什么操作，不实现什么操作，仅仅在这个类中具体实现就可以了。
"""

#先实现抽象的状态类：
class LiftState:
    def open(self):
        pass
    def close(self):
        pass
    def run(self):
        pass
    def stop(self):
        pass

#实现各个具体的状态类：
class OpenState(LiftState):
    def open(self):
        print("OPEN:The door is opened...")
        return self
    def close(self):
        print ("OPEN:The door start to close...")
        print ("OPEN:The door is closed")
        return StopState()
    def run(self):
        print ("OPEN:Run Forbidden.")
        return self
    def stop(self):
        print ("OPEN:Stop Forbidden.")
        return self

class RunState(LiftState):
    def open(self):
        print("RUN:Open Forbidden.")
        return self
    def close(self):
        print("RUN:Close Forbidden.")
        return self
    def run(self):
        print("RUN:The lift is running...")
        return self
    def stop(self):
        print("RUN:The lift start to stop...")
        print("RUN:The lift stopped...")
        return StopState()

class StopState(LiftState):
    def open(self):
        print ("STOP:The door is opening...")
        print ("STOP:The door is opened...")
        return OpenState()
    def close(self):
        print("STOP:Close Forbidden")
        return self
    def run(self):
        print("STOP:The lift start to run...")
        return RunState()
    def stop(self):
        print("STOP:The lift is stopped.")
        return self

#为在业务中调度状态转移，还需要将上下文进行记录，需要一个上下文的类。
class Context:
    lift_state=""
    def getState(self):
        return self.lift_state
    def setState(self,lift_state): # 把类对象传过来
        self.lift_state=lift_state

    def open(self):
        self.setState(self.lift_state.open())
    def close(self):
        self.setState(self.lift_state.close())
    def run(self):
        self.setState(self.lift_state.run())
    def stop(self):
        self.setState(self.lift_state.stop())

#在进行电梯的调度时，只需要调度Context就可以了。业务逻辑中如下所示：
def client():
    ctx = Context()
    ctx.setState(StopState()) # 初始状态为停止状态

    ctx.open()
    ctx.run()
    ctx.close()
    ctx.run()
    ctx.stop()

client()
#由逻辑中可知，电梯先在STOP状态，然后开门，开门时运行Run，被禁止，然后，关门、运行、停止。
