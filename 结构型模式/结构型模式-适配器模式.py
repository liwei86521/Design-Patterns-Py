# -*- coding:utf-8 -*-

#适配器模式：由于系统调用方式的原因，需要把不同类里面的方法（名字不一样），用同样的方式来调用
class Bird:
    def fly(self):
        print('bird is flying ...')

class Dog:
    def bark(self):
        print('dog is barking ...')

class People:
    def speak(self):
        print('people is speaking ...')

class Adapter:
    def __init__(self, clz_name, method):
        self.clz_name = clz_name
        self.__dict__.update(method) # *****
        #self.__dict__  {'clz_name': <__main__.Bird object at 0x000>, 'test': <bound method Bird.fly of <__main__.Bird object at 0x000>>}
        # print("self.__dict__ ",self.__dict__)


def test_fun():
    dog = Dog()
    bird = Bird()
    people = People()
    objects = []

    # dd = dict(test="123")  # dd --> {'test': '123'}
    # dd2 = dict("test" = "123")  # 报错
    objects.append(Adapter(bird, dict(test=bird.fly)))
    objects.append(Adapter(dog, dict(test=dog.bark)))
    objects.append(Adapter(people, dict(test=people.speak)))

    for object in objects:
        object.test()

    # Adapter(dog, dict(tes1t=dog.bark)).tes1t()
    # Adapter(bird, dict(tes2t=bird.fly)).tes2t()
    # Adapter(people, dict(tes3t=people.speak)).tes3t()

test_fun()

"""
bird is flying ...
dog is barking ...
people is speaking ...
"""
