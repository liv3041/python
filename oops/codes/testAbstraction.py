

"""
Abstarction

Abstraction helps you to hide internal implementation details which are unnecessary
for the user. This enables users to do complex task into more easy logic without understanding
the hidden codes.

Abstarct class declared with method without utilization.
FOR implementation we declare a derived class.

Also called as "ABC" - Abstract Base Class

Its utilization is dne in two ways:
- Abstract method
- Abstract class

Data Abstarction = Data Encapsulation + Information Hiding

Abstract Method
- Methods without implementation.
- Decorate require MetaClass (ABCMeta) to be present
- abstractmethod() may be used to declare abstract methods.
"""




from abc import ABCMeta, abstractmethod

class Pet(metaclass = ABCMeta):
    @abstractmethod
    def pet_say(self):
        return("I have a Pet!")

class Dog(Pet):
    def pet_say(self):
        s = super(Dog,self).pet_say()
        return print("%s - %s" % (s,"Horf!!"))

d = Dog()
d.pet_say()