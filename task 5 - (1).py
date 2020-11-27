def get():
    first_integer=int(input("enter the 1st integer: "))
    second_integer=int(input("enter the 2nd integer: "))
    addition=first_integer+second_integer
    print("Addition of two numbers is "+str(addition))
    subtraction=first_integer-second_integer
    print("Subtraction of two numbers is "+str(subtraction))
    division=first_integer/second_integer
    print("Division of two numbers is "+str(division))
    multiplication=first_integer*second_integer
    print("Multiplication of two numbers is "+str(multiplication))

print("enter two integers to add, subtract , multiply and divide")
get()
