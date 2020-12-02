import re
def check(text):
        patterns = '\d$'
        if re.search(patterns,  text):
                return ("There is a number at the end of the text!")
        else:
                return('No number at the end of the text!')

print("give a text to find whether a number is present at the end or not!")
text=input("enter a text: ")
print(check(text))
