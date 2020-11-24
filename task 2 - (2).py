Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string="ankel"
>>> string=string.replace("k","g")
>>> print(string)
angel
>>> string1=string.replace(string[2],"g")
>>> print(string1)
angel
>>> #index 2 is used to replace the 3rd character of the string since index value starts from 0 