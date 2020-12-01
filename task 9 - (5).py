#to count the total number of even numbers in a list
n=int(input("how many numbers you want to input in a list: "))
list1=[]
count=0
for i in range(n):
    inputs=int(input("enter the number: "))
    list1.append(inputs)
print("So the created list is: ",list1)
for j in list1:
    check=lambda j:j%2==0
    if(check(j)==True):
        count+=1
print("There are ",count," even numbers in the list")
    
