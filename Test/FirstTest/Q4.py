area=int(input("Enter area of one wall"))
int_cost=int(input("Enter interoer wall cost "))
ext_cost=int(input("Enter exterior wall cost"))
cost_int=area*8*int_cost
cost_ext=area*6*ext_cost
#To calculte area of total cost
#First calculate total cost
Total_cost=cost_int+cost_ext
print("Interior painting cost=",cost_int)
print("Exterior painting cost=",cost_ext)
print("Total painting cost=",Total_cost)
