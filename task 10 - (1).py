import re
def check(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print("when string with characters (a-z and A-Z) and(or) numbers is inputted , 'true' gets printed else 'false' gets printed") 
string=input("enter your input: ")
print(check(string)) 

