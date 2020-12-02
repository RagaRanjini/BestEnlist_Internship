import re
def check(word):
        if re.search('ab',word):
                return ('Found a match!')
        else:
                return('Not matched!')

word=input("enter your word or text to find whether 'ab' is present: ")
print(check(word))
