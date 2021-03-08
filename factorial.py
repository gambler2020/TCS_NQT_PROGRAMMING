#without command line program
n=int(input("Enter a number: "))
#print(type(n))
x=1
for i in range(1, n+1):
    x=i*x
print("Factorial is: {}".format(x))
