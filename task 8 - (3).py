a=int(input("enter one integer: "))
try:
    print(b)
except NameError:
    print("NameError has occured . check the variables assigned .....")
else:
    print("Some other error has occured ....")
