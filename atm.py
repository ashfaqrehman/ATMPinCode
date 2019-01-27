#!/usr/bin/env python
print("Hello!")
trys=1
pin="1234"
while True: 
    user_input = input("Please enter your PIN: ")  
    print(f'You entered: {user_input}')  
    if trys == 3:
        print("Account locked. The police is on its way.")
        break
    elif user_input == pin:
        print("Your account balance is: 0. Goodbye!")
        break
    else:
        trys += 1
        
