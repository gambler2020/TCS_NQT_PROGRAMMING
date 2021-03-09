interior=int(input("Enter the number of interior walls: "))
exterior=int(input("Enter the number of Exterior walls: "))
add_int=0
add_ext=0
if interior==0 and exterior==0:
    print("User may don't want to paint the wall")
elif interior>=0 or exterior>=0:
    for i in range(interior):
       n=float(input("Enter interior walls area: "))
       add_int=add_int+n
    for j in range(exterior):
       m=float(input("Enter exterior walls area: "))
       add_ext=add_ext+m

cost_int=add_int*18
cost_ext=add_ext*12
total_cost=cost_int+cost_ext
print("Total estimates Cost : {} INR".format(round(total_cost,2)))
