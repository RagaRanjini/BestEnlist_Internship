#to find numbers divisible by 9 from a list of numbers
list1=[]
n=int(input("how many integers you want to put in a list: "))
for i in range(n):
    inputs=int(input("enter the integer: "))
    list1.append(inputs)
print("List created by user is: ",list1)
for j in list1:
   list2=list(filter(lambda j:(j%9==0),list1))
print("list of integers divisible by 9 is: ",list2)
