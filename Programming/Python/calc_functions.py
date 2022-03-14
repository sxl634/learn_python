# Function module for calculator application in Python: Next Steps    
    
# Factorial function:
def factorial(n):
    try:
        n=int(n)
    except:
        return "--> Error!"

    # '0' is special:
    if n == 0:
        return 1

    # back out if too large:
    if n > 37:
        return "--> Answer will not fit on screen!"

    #catch negative numbers:
    if n < 0:
        return "--> Error!"

    #apply factorial algorithm 
    ans=n # set initial value of answer before loop
    while n>1:
        ans=ans*(n-1)
        n=n-1
    return ans

# Convert to roman numerals function:
def to_roman(n):
    try:
        n = int(n)
    except:
        return "--> Error!"
    # opt out of numbers greater 4999:
    if n > 4999:
        return "--> out of range"

    # create the tuple and dictionary:
    numberBreaks = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    letters = {1000 : "M", 900 : "CV", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 : "L", 40 : "XL", 10 : "X", 9 : "IX", 5 : "V", 4 : "IV", 1 : "I" }

    # start the algorithm:
    result = ""
    for value in numberBreaks:
        while n>= value:
            result = result+letters[value]
            n = n-value
    return result

# Convert base 10 numbers to binary function:
def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "--> Error!"

# Convert base 2 numbers to base 10 function:
def from_binary(n):
    try:
        return int(n, 2)
    except:
        return "--> Error!"
