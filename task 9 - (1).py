#create a lambda function that multiplies argument x with argument y
def function(y):
    return lambda x : x * y
x=int(input("enter x : "))
y=int(input("enter y : "))
val_x=function(y)
print("x multiplying with y gives:",val_x(x))
