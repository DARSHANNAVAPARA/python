# how to create a class? 
# what is class?
#class is the set of entities with properties and methods
#class makes programmers to work easily
#for exmaple -> our class is human then there are two element 
# first is properties and secound is the methods 
# in human there are same properties like name and occupation 
#there are several methods like do work ,speak and walk etc.
class human:
    def __init__(self,n,o,a):
        self.name=n
        self.occupation=o
        self.age=a
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots a film")
        elif self.occupation=="ai enginner":
            print(self.name,"is a ai engineer")   
    def speaks(self):
        print(self.name,"says how are you")
    def age(self):
        if self.age==20:
            print(self.name,"is a mature ")     
x=human("akshay","actor","50")                     
x.do_work()
x.speaks()
x.home


y=human("henil","tennis player","18")
y.do_work()
y.speaks()
y.age
z=human("darshan","ai engineer","204")
z.do_work()
z.speaks()
z.age()