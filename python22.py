# Create multiple inheritance on teacher,student and youtuber.
#Q. if we have created teacher and now one student joins master 
#degree with becoming teacher then what??

#Ans :  just make subclass from  teacher so that student will 
#become teacher.
class teacher:
    def teaching(self):
        print("i like teaching")
class youtuber:
    def vidios(self):
        print("i like to make new vidios")
class student(teacher,youtuber):
    def to_study(self):
        print("i like to study new things")
s=student()

print(isinstance(s,teacher))
print(issubclass(s,youtuber))                       