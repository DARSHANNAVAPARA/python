# what is inheritance??
# there are some amount of classes that inherit the class is called inheritance
#for  example-> vehicle. the main purpose of vehicle is to provide a traspotation.so 
#here vehicle is the class so there are two vehicle first is car and secound is bike 
#car as roof and 4 wheels whereas bike as no roof and 2 wheels .
#bike is use for roadtrip and car is use for family long trip.
class vehicle:
    def general_useage(self):
        print("general use:transportation")
class car(vehicle):
    def __init__(self):
        print("i am car")
        self.wheels=4
        self.roof=True
    def sepecific_useage(self):
        self.general_useage()
        print("specific use: vacation with family")
class bike(vehicle):
    def __init__(self):
        print("i am bike")
        self.wheels=2
        self.roof=False
    def sepecific_useage(self):
        self.general_useage()
        print("specific use:roadtrip and racing")    
c=car()
#here "is subclass" is use to check whether the car is subclass of parent class that is vehicle

print(issubclass(car,vehicle))
# here isinstance is use to check whether elememnt b is present in bike or not
b=bike()
print(isinstance(b,bike))
                  





