indian=["roti","daal","rice","milk"]
chinese=["nodles","bhel","manchurian"]
american=["pizza","burger","sandwich"]

dish=input("enter any dish:")
if dish in indian:
    print("the dish is indian")
elif dish in chinese:
    print("the dish is chinese")
elif dish in american:
    print("the dish is american")
else:
    print("i dont know the dish")         