# how to swap a list
def swaplist(newlist):
    size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
newlist=[1,2,3,4,5,6,7,80]
print(swaplist(newlist))