#basic arithmetic calculations
def add():
    n=int(input("how many integers do you want to add? : "))
    sum=0
    for i in range(n):
        a=int(input("enter the integer to add: "))
        sum+=a
    print("addition of given integers gives = ",sum)
def sub():
    print("give two integers:-")
    num1=int(input("enter the 1st integer: "))
    num2=int(input("enter the 2nd integer: "))
    print("subtraction of 2nd integer from 1st integer = ",num1-num2)
def mul():
    n=int(input("how many integers do you want to multiply? : "))
    mul=1
    for i in range(n):
        b=int(input("enter the integer to multiply: "))
        mul=mul*b
    print("multiplication of given integers gives = ",mul)
def div():
    print("give two integers:-")
    num1=int(input("enter the 1st integer: "))
    num2=int(input("enter the 2nd integer: "))
    print("division of 1st integer and 2nd integer = ",num1/num2)
print(" calculations accessible : \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division")
choice=int(input("enter your choice: "))
if(choice==1):
    add()
elif(choice==2):
    sub()
elif(choice==3):
    mul()
elif(choice==4):
    div()
else:
    print("wrong input")
