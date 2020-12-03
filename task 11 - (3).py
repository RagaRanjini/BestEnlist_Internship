#Using sorted() function,to sort the list in ascending order.
my_list=[]
given_range=int(input("how many elements you wish to add in your list: "))
for i in range(given_range):
    inputs=input("enter your input: ")
    my_list.append(inputs)
print("so the given list by user is: ",my_list)
my_list.sort()
print("sorting the above list in ascending order , we get the following list: ",my_list)
    
