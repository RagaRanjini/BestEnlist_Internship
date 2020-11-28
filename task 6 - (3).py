#fibonacci sequence upto nth term
n=int(input("enter how many terms to be printed: "))
num1=0
num2=1
count=0
if(n<=0):
    print(" INVALID ! ")
elif(n==1):
    print("fibonacci series upto ",n," st term:")
    print(num1)
else:
    print("fibonacci series upto ",n," th term :")
    while(count<n):
        print(num1)
        num3=num1+num2
        num1=num2
        num2=num3
        count+=1
