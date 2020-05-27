def commissionCalc(sales):
    if sales>100:
        return sales*100
    elif sales>50:
        return sales*50
    elif sales>20:
        return sales*20
    else:
        return 0
def salaryCalc(basic,sales):
    grossSalary = basic + commissionCalc(sales)
    print(f"your gross salary is {grossSalary}")
salaryCalc(50000,150)
#while loop for iterative tasks where user can terminate at any point
a=0
flag = True
favFoods=[]
while flag:
    userinput=input("enter fav foods: ")
    if userinput=='Q':
        flag=False
    else:
        favFoods.append(userinput)
        #print(f"{a} inside while loop")
    #a+=1
print(favFoods)

