n=int(input("enter total number of integers to be in list: "))
list=[]
for i in range(0,n):
    input_integer=int(input("enter the integer: "))
    list.append(input_integer)
print("The list obtained is: ",list)
#adding an item to the list
list.append(int(input("integer to append: ")))
print("after adding the given integer to the list , the list will be like : ",list)
#removing an item from the list
list.remove(int(input("integer to delete: ")))
print("after removing the given integer , list will be like : ",list)
#removal specifying index value
index=int(input("index at which integer to be deleted: "))
if(index>=n):
    print("no integer present")
else:
    list.remove(list[index])
    print("after removing the integer at the given index , list will be like : ",list)
#to find the maximum
maximum=max(list)
#maximum of the list is stored in variable "maximum"
print("The maximum of the list is ",maximum)
#to find the minimum
minimum=min(list)
#minimum of the list is stored in variable "minimum"
print("The minimum of the list is ",minimum)
#to delete the list
list.clear()
print("after deleting the list, we have : ",list)
    
    
