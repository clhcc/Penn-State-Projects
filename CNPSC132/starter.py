# 10/08 Quiz 1 - Coding Part
# Name: Linhan Cai
#

import math   # you can use math.pi
import cmath

##QUESTION 1

from abc import *

class Figure(ABC):
    
    '''
    Doctest:
    >>> a=Figure(6) 
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: Can't instantiate abstract class Figure with abstract methods area, perimeter
    >>> a=Circle(9)
    >>> a.perimeter        # 2*pi*r
    56.548667764616276
    >>> a.area          # pi*r**2
    254.46900494077323
    >>> a=Rectangle(2,5) 
    >>> a.perimeter     #2*(w + h)
    14
    >>> a.area    # w * h
    10
'''
    
    def __init__(self, side):
        super().__init__()
        self.side = side

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Figure):
    def __init__(self, w, h):
        super().__init__(w)
        self.w = w
        self.h = h

    @property
    def perimeter(self):
        return 2 * (self.w + self.h)

    @property
    def area(self):
        return self.w * self.h

class Circle(Figure):
    def __init__(self, r):
        super().__init__(r)
        self.r = r

    @property
    def perimeter(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r ** 2



##QUESTION 2
class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Line:
    '''
    Doctest:
    >>> p1=Point2D(-7,-9)
    >>> p2=Point2D(1,5.6)
    >>> line1=Line(p1,p2)
    >>> line1.distance
    16.648
    >>> line1.midpoint
    (-3.0, -1.7)
    >>> p1=Point3D(1,2,3)
    >>> p2=Point3D(4,5,5)
    >>> line2=Line(p1,p2)
    >>> line2.distance
    4.69
    >>> line2.midpoint
    (2.5, 3.5, 4.0)
'''
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    @property
    def distance(self):
        if isinstance(self.point1, Point2D) and isinstance(self.point2, Point2D):
            d = (self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2
            return round(math.sqrt(d), 3)

        if isinstance(self.point1, Point3D) and isinstance(self.point2, Point3D):
            d2 = (self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2 + (self.point2.z - self.point1.z) ** 2
            return round(math.sqrt(d2), 3)

    @property
    def midpoint(self):
        if isinstance(self.point1, Point2D) and isinstance(self.point2, Point2D):
            return (round((self.point1.x + self.point2.x) / 2, 1) , round((self.point1.y + self.point2.y) / 2, 1))

        if isinstance(self.point1, Point3D) and isinstance(self.point2, Point3D):
            return (round((self.point1.x + self.point2.x) / 2, 1) , round((self.point1.y + self.point2.y) / 2, 1), round((self.point1.z + self.point2.z) / 2, 1))
