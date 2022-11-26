import re

def isValid(n):
    num = re.compile("^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$")
    return num.match(n)
    
n =  input()
if (isValid(n)):
    print("Valid number")
else:
    print("Invalid number")