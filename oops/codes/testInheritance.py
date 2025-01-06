# Single Inheritance
# class Family:
#     name = ""

#     def __init__(self,name):
#         self.name = name
    
#     def printName(self):
#         print("Name:"+ self.name)

# class Relative(Family):
#     def __init__(self,name):
#         self.name = name
    
#     def doPython(self):
#         print("Pro in Python")

# brian = Family("Brian")
# brian.printName()
# joy = Relative("Joy")
# joy.printName()
# joy.doPython()

# Multiple Inheritance

# class Father:
#     def __init__(self):
#         super(Father,self).__init__()
# print("Father of the Son")

# class Mother(object):
#     def __init__(self):
#         super(Mother,self).__init__()
# print("Mother of the Son")

# class Son(Mother,Father):
#     def __init__(self):
#         super(Son,self).__init__()
# print("Son of Father and Mother")

# MultiLevel Inheritance:
class Animal:
    def cat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

d = Puppy()
d.cat()
d.bark()
d.weep()