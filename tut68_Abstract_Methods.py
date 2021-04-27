# from abc import ABCMeta, abstractmethod  # if we have 3.4 version and above we can write this line as given below
from abc import ABC, abstractmethod


# class Shape(metaclass=ABCMeta): see to  line 1 ,for line 1 we have to write like this
class Shape(ABC):  # for line 2 we have to write like this
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 5
        self.breadth = 6

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())

# shapeobj = Shape()  # we cannot create object of abstract class
