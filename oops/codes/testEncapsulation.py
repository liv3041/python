"""
Encapsulation

- Encapsulation is used to hide data being accessed by unauthorized parties.
- Hiding of data structures is done by methods and variables.

class = methods + variables

methods and variables := Can be public, private and protected

Private Methods:

- Class methods should be prefixed with double underscores
Eg: def __earth(self)
        print("This is an absurd planet. A planet of randomness and grief.")

Private Variable:

- When a piece of information is required to remain unchanged throughout the program,
  variable can be decalred as private.
- Class variables should be prefixed with double underscores.
- Advantage:= Information the private variable contains can only be changed
              within the class containing the variable.

Example: __run = 123

"""

class Car:

    __topspeed = 0
    __name = ""

    def __init__(self):
        self.__fuel()
        self.__topspeed = 20
        self.__name = "Volvo"
    def drive(self):
        print("Driving..!!")
        print("Driving "+str(self.__name) + " at the speed of " + str(self.__topspeed)+ " km/h" )
    def __fuel(self):
        print("Refilling Gas")

volvo = Car()
volvo.drive()

# Cannot access private method directly through object
# volvo.__fuel()

# To access private method fuel.
volvo._Car__fuel() 


""""
Getters and Setters

Getter Method
- private variables can be accessed using getter method through object declaration.
  Syntax:= obj.getRun

Setter Method
- private variables can be accessed using setter method through object declaration.
  Syntax: obj.setRun


"""
print("******************************")

class car(object):
    def __init__(self):
        self.__milage =16
    def getMilage(self):
        print(self.__milage)
    def setMilage(self, milage):
        self.__milage = milage

volvo = car()
volvo.getMilage()
volvo.setMilage(20)
volvo.getMilage()

