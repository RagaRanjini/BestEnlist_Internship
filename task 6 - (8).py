import math
print("choose your option to solve :\n 1.sin \n 2.cos \n 3.tan \n 4.to find gcd")
n=int(input("enter your choice: "))
if(0<n<4):
    x=int(input("enter degree: "))
    if(n==1):
        val=math.sin(x)
        print("sin(",x,") = ",val)
    elif(n==2):
        val=math.cos(x)
        print("cos(",x,") = ",val)
    else:
        val=math.tan(x)
        print("tan(",x,") = ",val)
    
elif(n==4):
    a,b=int(input("enter 1st integer: ")),int(input("enter 2nd integer: "))
    val=math.gcd(a,b)
    print("GCD of ",a," and ",b," is ",val)
else:
    print("invalid choice")
    
