#!/usr/bin/env python
print("Hello!")

while True: #start value
    try:
        user_input = input("Enter a start value (Default: 0): ") or 0
        startvalue = int(user_input)
        print("startvalue is: ", startvalue)
        break
    except ValueError:
        print("Oops! Bad value! Please enter a number.")
while True: #step value
    try:
        user_input = input("Enter a step value (Default: 1): ") or 1
        stepvalue = int(user_input)
        print("stepvalue is: ", stepvalue)
        break
    except ValueError:
        print("Oops! Bad value! Please enter a number.")    
while True: #end value
    try:
        user_input = input("Enter an end value: ") 
        endvalue = int(user_input)
        print("endvalue is: ", endvalue)
        break
    except ValueError:
        print("Oops! You must provide an end value.")       
lst = list(range(startvalue,endvalue+1,stepvalue))
print ("The number are: ",lst)