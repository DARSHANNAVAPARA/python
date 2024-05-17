# how to swap list last and first element
def swaplist(list):
    first=list.pop(0)
    last=list.pop(-1)
    list.insert(0,last)
    list.append(first)
    return list
newlist=[3,4,5,6,7,8,9]
print(swaplist(list))