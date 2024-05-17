#all about function
def calculate(cost):
    total=0
    for item in cost:
        total=total+item
        return total
darshans_cost=[5000,10000,15000,20000]
    toms_cost=[2000,3000,5000,10000]
    darshan_totol=calculate(darshans_cost)
    toms_total=calculate(toms_cost)
    print(darshan_totol)
    print(toms_totat)