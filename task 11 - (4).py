#To create a program using filter function,to filter the even numbers so that only odd numbers are passed to the new list.

def to_filter(integer):
    if(integer%2!=0):
        return True
    else:
        return False
print("YOU CAN CREATE A LIST CONTAINING ANY INTEGER , AFTER THE EXECUTION OF CODE , ODD INTEGERS FROM YOUR LIST ALONE GETS PRINTED USING FILTER()")
my_list=[]
lmt=int(input("how many integers you wish to input to your list: "))
for i in range(lmt):
    inputs=int(input("enter your integer: "))
    my_list.append(inputs)
new_list=list(filter(to_filter,my_list))
print("THE FILTERED LIST CONTAINING ONLY ODD INTEGERS IS: ",new_list)
