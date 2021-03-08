n=int(input())
if n<=2000 and n>0:
    print("Time Estimated: 25 minutes")
elif n>=2001 and n<=4000:
    print("Time Estimated: 35 minutes")
elif n>4000 and n<=7000:
    print("Time Estimated: 45 minutes")
elif n==0:
    print(0)
else:
    print("INVALID INPUT")
