# what is the multiprocessing in python langauge 
# we can handle multiple task as a same time in the program
import multiprocessing.process
import time
import multiprocessing
def square_number(numbers):
    for i in numbers:
        print(i*i)
def cube_number(numbers):
    for i in numbers:
        print(i*i*i)
numbers=[2,3,8,9]
p1=multiprocessing.process(target=square_number,args=(numbers,))
p2=multiprocessing.process(target=cube_number,args=(numbers,))              
p1.start()
p2.start()
p1.join()
p2.join()
