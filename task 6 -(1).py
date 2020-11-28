#user can give inputs to this code
print("choice: \n1.user can give inputs \n 2.can use default list coded already")
x=int(input("enter your choice: "))
if (x==1):
    print("user must give inputs to get their values each added by 2")
    list1=[]
    list2=[]
    n=int(input("Total number of elements to be added to the list: "))
    for i in range(n):
        inputs=int(input("enter the integer: "))
        list1.append(inputs)
        list2.append(inputs+2)
    
    print("List created by user: ",list1)
    print("Incrementing +2 to each integer in the user's list we get: ",list2)

#when a list is already created
elif(x==2):
    list3=[1,2,3,4,5]
    print("defaultly given list is: ",list3)
    list4=[]
    for i in list3:
        list4.append(i+2)
    print("Incrementing +2 to each integer in the default list, we get: ",list4)

else:
    print("wrong choice")
