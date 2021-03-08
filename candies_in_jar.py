c=int(input("Enter number of candies you want to buy: "))
if c<=5 and c>0:
    print("NUMBER OF CANDES SOLD : {}".format(c))
else:
    print("INVALID INPUT")
a=10-c
print("NUMBER OF CANDIES LEFT : {}".format(a))
