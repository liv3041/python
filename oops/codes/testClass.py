class Car:
    car_type = "suv"
    model = "890"
    milage = "60km/h"
   
    
    def __init__(self,name):
        print("This is a parameterized constructor")
        self.name = name
    # def __init__(self):
    #     print("This is a non-parameterized constructor",self.name)
    
    def model(self,name):
        print("My first Car: ",self.name)
    def start(self):
        print("Car started")
    def reverse(self):
        print("Car taking reverse")
    
    def __del__(self):
        print("The constructor is destroyed with the help of destructor.")

def main():
    volvo = Car("Volvo S90")
    volvo.start()
    volvo.reverse()
    print(volvo.car_type)
    volvo.model("Volvo 890")
    del volvo

if __name__ == "__main__":
    main()
    