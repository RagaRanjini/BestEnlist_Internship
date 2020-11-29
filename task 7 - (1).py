#to create a module and implement it in another py file
#I have uploaded my module in github as "module"


import module
print("Language list is created")
choice=input("do you wish to add any other language (y-yes/n-no) :")
c=[]
if(choice=='y' or choice=='Y'):
    b=int(input("how many languages you want to add in list : "))
    for i in range(1,b+1,1):
        d=input("ENTER  THE LANGUAGE: ")
        c.append(d)
    module.newlist(c)   
else:
    module.newlist()


