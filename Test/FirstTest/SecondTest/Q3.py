n=int(input("Enter number of employee"))
tot_sal=0
for i in range(1,n+1):
    sal=int(input("Enter salary of employee"))
    if sal < 20000:
        da=sal *10/100
        ta=sal*12/100
        hra=sal*15/100
    else:
        da=sal *10/100
        ta=sal*12/100
        hra=sal*15/100
    salary=sal+da+ta+hra
    print("Salary of employee",n,"is",salary)
    tot_sal=tot_sal+salary
print("Total salary is=",tot_sal)
