#fibonacci series to n
last_val=int(input("Enter an integer upto which you want to print fibonacci series :"))
val1,val2=0,1
print(val1)
print(val2)
val=0
while(val<last_val):
    operation=lambda val1,val2:val1+val2
    if(operation(val1,val2) <= last_val):
        print(operation(val1,val2))
    val=val1+val2
    val1=val2
    val2=val
