#how to do search operation in array in python dsa
def findelement(arr,n,key):
    for i in range(n):
        if (arr[i]==key):
            return i
    return -1
arr=[4,5,5,5,5,5,5,8,7]
n=len(arr)
key=8
index=findelement(arr,n,key)
if index !=-1:
    print(index+1)
else:
    print("element is not found")


    
