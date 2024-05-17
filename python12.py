# how to swap first and last element in tuple
def swaplist(list):
    get=list[0],list[-1]
    list[-1],list[0]=get
    return list
list=[2,4,6,8,10]
print(swaplist(list))
