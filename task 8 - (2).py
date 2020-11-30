print("INSTRUCTION: \n press 1 to add your inputs \n press 2 to subtract your inputs \n press 3 to multiply your inputs \n press 4 to divide your inputs")
choice=int(input("enter your choice: "))
a=input("give your 1st input: ")
b=input("give your 2nd input: ")
if(choice==1):
        try:
            add=int(a)+int(b)
            print("addition of ",a," and ",b," gives: ",add)
        except:
            print("give integers to add !!!")
elif(choice==2):
        try:
            sub=int(a)-int(b)
            print("subtraction of ",a," and ",b," gives: ",sub)
        except:
            print("give integers to sub !!!")
elif(choice==3):
        try:
            mul=int(a)*int(b)
            print("multiplication of ",a," and ",b," gives: ",mul)
        except:
            print("give integers to multiply !!!")
elif(choice==4):
        try:
            div=int(a)/int(b)
            print("division of ",a," and ",b," gives: ",div)
        except:
            print("give integers to divide !!!")
else:
    print("wrong choice !!!")
