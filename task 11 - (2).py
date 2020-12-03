#To create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
list1=[]
list2=[]
print("since range is given from 1 to 8 , please input 8 elements to the list!!!")
for i in range(1,9,1): #9 is given , so that the range accepts upto 8
    inputs=input("enter your input : ")
    list1.append(inputs)
    list2.append(i)
print("NEW LIST OF TUPLES AFTER MERGING USER'S LIST AND RANGE TOGETHER IS: ",list(tuple(zip(list1,list2))))






