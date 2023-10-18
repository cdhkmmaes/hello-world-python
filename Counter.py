import abc
from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self):
        self.__number = 0

    # def incrementCounter(self):
    #     self.__number+=1
    def incrementCounter(self, delta):
        self.__number += delta

    # def decrementCounter(self):
    #     self.__number-=1
    def decrementCounter(self, delta):
        self.__number -= delta

    def getCounterValue(self):
        return self.__number

    def reset(self):
        self.__number = 0

    def __str__(self):
        # return('Counter number={self.__number}')
        return 'Counter number=' + str(self.__number)

    @abstractmethod
    def inc(self):
        pass

    @abstractmethod
    def dec(self):
        pass


def foo():
    print('foo!!!')


class SimpleCounter(Counter):
    def __init__(self):
        super().__init__()

    def inc(self):
        super().incrementCounter(1)

    def dec(self):
        Counter.decrementCounter(self,1)


foo()
foo()
foo()
c = SimpleCounter()
print(c)
# print(c.getCounterValue())
# print(c.__number)
c.incrementCounter(1)
print(c)
# print(c.getCounterValue())
c.decrementCounter(2)
print(c)
c.incrementCounter(999)
print(c)
c.inc()
print(c)
c.inc()
print(c)
# c.dec()
# print(c)
