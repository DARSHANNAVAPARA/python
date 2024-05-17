# for a given list of numbers find the square and cube of every numbers
#to find it we will first try to make a function
def square_numbers(numbers):
    for i in numbers:
        print(i*i)
def cube_numbers(numbers):
    for i in numbers:
        print(i*i*i)        
        

numbers=[1,2,3,4,5]
square_numbers(numbers)
cube_numbers(numbers)
