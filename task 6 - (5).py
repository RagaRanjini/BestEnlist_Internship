#multiplication table of 9
n=int(input("enter a number upto which 9 must be multiplied: "))
if(n<=0):
    print(" INVALID ")
else:
    for i in range(1,n+1,1):
        print("9 * ",i," = ",9*i)
        
