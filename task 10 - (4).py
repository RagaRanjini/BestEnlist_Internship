import re
input=input("enter your input: ")
results = re.finditer(r"([0-9]{1,3})",input)
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))
	 
#if the length of the number is more than 3, then number gets splited and gets printed in next line
	 
