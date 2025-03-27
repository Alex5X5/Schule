import inspect
from abc import ABC
from symtable import Class

"""
    .
"""


class SuperClass(ABC):
    def ovv_method(self):
        pass

    def __init_subclass__(cls):
        print('method_1' in cls.__dir__(cls))
        if 'method_1' in cls.__dir__(cls):
            print('has')
            print(cls.__getattribute__(cls, 'method_1'))
            print(inspect.getsource(cls.__getattribute__(cls, 'ovv_method')))
        else:
            print('not')


class SubClass1(SuperClass):

    def ovv_method(self):
        print('subclass1')

    def method_1(self):
        pass


# defining another subclass
class SubClass2(SuperClass):
    def method_1(self):
        pass


# references for subclasses
subClass1 = SubClass1()
subClass2 = SubClass2()

class Test:
    """
        .
    """

    def __subclasshook__(cls, __subclass):
        pass

    def __str__(self):
        return "<Schule.M01.Main.Test>"

    def __init__(self):
        print('init')

print(Test())