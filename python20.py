# create a inheritance on animal and dog
#for example, 
    #Animal and Dog both has same habitat so create a method for habitat 
class animal:
    def general_useage(self):
        print("general useage:for entaintement")
class dog(animal):
    def __init__(self):
        print("i am dog")
        self.can_be_pet=True
        self.low_cost=True
    def specific_use(self):
        print("use for private house pet")
class tiger(animal):
    def __init__(self):
        print("i am tiger")
        self.can_be_pet=False
        self.low_cost=False
    def specific_use(self):
        print("it can not be use as pet for home")
d=dog()
d.general_useage()
d.specific_use()
t=tiger()
t.general_useage()                  
t.specific_use()

            

