#multiply each number in given list with given number
n=int(input("how many integers you want to give to the list: "))
list1=[]
for i in range(n):
    inputs=int(input("enter the integer: "))
    list1.append(inputs)
print("so the given list by the user is: ",list1)
x=int(input("what number you wish to get multiplied with each integers in the above list: "))
for j in list1:
    list2=list(map(lambda j:j*x,list1))
print("after multiplying ",x," with each integers in the list , we get the following list: ",list2)





