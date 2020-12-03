# using zip() function and list() function, create a merged list of tuples from the two lists given.
list1=[]
list2=[]
a=int(input("how many elements you wish to add in list1: "))
for i in range(a):
    input1=input("enter your input for list1: ")
    list1.append(input1)
b=int(input("how many elements you wish to add in list2: "))
for j in range(b):
    input2=input("enter your input for list2: ")
    list2.append(input2)
print("list1 you created is: ",list1)
print("list2 you created is: ",list2)
result=list(tuple(zip(list1,list2)))
print("THE RESULTANT MERGED LIST OF TUPLES IS: ",result)
