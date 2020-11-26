
#tuple is created directly
def choice1():
    #tuple1 is to get the reversed of tuple that contains some default integers
    tuple1=(5,10,15,20)
    print("orginal tuple : ",tuple1)
    reversed_tuple=tuple(reversed(tuple1))
    print("reversed tuple : ",reversed_tuple)
    #tuple_char is to get the reversed of tuple that contains some default characters
    tuple_char=('a','b','c','d')
    print("orginal tuple : ",tuple_char)
    reversed_tuple=tuple(reversed(tuple_char))
    print("reversed tuple : ",reversed_tuple)

#to get the values from user and add it to tuple
def choice2():
    list=[]
    n=int(input("enter total number of elements to be in tuple: "))
    for i in range(0,n):
        #int datatype is not used to get input , so ,character/string is acceptable
        inputs=input("enter the element: ")
        list.append(inputs)
    tuple2=tuple(list)
    print("tuple: ",tuple2)
    print("reversed tuple : ",tuple(reversed(tuple2)))

print("hello ! choose an option to get reversed tuple :- \n choose 1 to get default tuple \n choose 2 to enter your values to tuple \n choose 3 to try both ")
a=int(input("enter your choice: "))
if(a==1):
    choice1()
elif(a==2):
    choice2()
elif(a==3):
    choice1()
    choice2()
else:
    print("wrong input !")
