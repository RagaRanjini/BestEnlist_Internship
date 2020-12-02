import re
def check(string):
    charRe = re.compile(r'[^A-Z]')
    string = charRe.search(string)
    return not bool(string)

print("when string with uppercase characters is inputted , 'true' gets printed else 'false' gets printed") 
string=input("enter your input: ")
print(check(string)) 
