
""""

Operator Overloading:
Python program that grants same opertor to handle different value in background.

Types of operator overloading:

Operators            Function                Method Description
    +             __add__(self,other)              Addition
    -             __sub__(self,other)              Subtraction
    *             __mul__(self,other)              Multiplication
    /             __truediv__(self,other)          Division
    %             __mod__(self,other)              Remainder
    <             __it__(self,other)               Less than
    <=            __le__(self,other)               Less than or Equal-to
    ==            __eq__(self,other)               Equal to
    !=            __ne__(self,other)               Not equal-to
    >             __gt__(self,other)               Greater than
    >=            __ge__(self,other)               Greater than or Equal-to
    [index]       __getitem__(self,index)          Index operator
    str           __str__(self)                    String Representation

"""



a = 5
b = 500
c = a+b
print(c)

x = "man"
y = "sion"
z = x + y
print(z)


print ("************************************")

class Circle:
    def __init__(self,radius):
        self.__radius = radius
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    
    def area(self):
        return math.pi * self.__radius ** 2
    
    def __add__(self,another_circle):
        return Circle(self.__radius + another_circle.__radius)
    
    def __sub__(self,another_circle):
        return Circle(self.__radius - another_circle.__radius)

c1 = Circle(8)
print(c1.getRadius())

c2 = Circle(10)
print(c2.getRadius())

c3 = c1 + c2
print(c3.getRadius())

c3 = c2 - c1
print(c3.getRadius())

""""
Polymorphism

- Provision of a single interface to entities of different types.
- One operation which can be applied to some other type or types.

Method Overloading:

- Same method or function name.
- Different data type and parameters.

Ways to call a method (Method Overloading):
- method(p)
- method(p,q)
- method(p,q,r)

"""
print ("************************************")
class Man:
    def sayHi(self, name = None):
        if name is not None:
            print("Hi! " + name)
        else:
            print("Hi")

obj = Man()
obj.sayHi()
obj.sayHi("Hello World!")
print ("************************************")

"""

Method Override:
- Same method or function name in subclass.
- Override for different tasks.

Ways to call a method (Method overloading):
- superclass A() calling - method A()
- subclass B() calling - method A() 

"""

class Triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def getArea(self):
        print(self.base * self.height/2, "is area of triangle.")


class Square(Triangle):
    def __init__(self,side):
        self.side = side
        Triangle.__init__(self,side,side)

    def getArea(self):
        print(self.side * self.side, "is area of square")

t = Triangle(2,6)
s = Square(4)
t.getArea()
s.getArea()

    