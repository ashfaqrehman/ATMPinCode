# Part 2: Write an ATM pin code prompt
Write a program that asks the user for their PIN number. The valid PIN number is "1234". The user has 3 attempts to enter the correct pin until they are locked out of their account. If the correct value is entered, a message is printed and the program ends.
There is no fixed input/output, but here is an example of an expected flow.

Please enter your PIN: 2222
Invalid pin
Please enter your PIN: 1234

Your account balance is: 0. Goodbye!


Please enter your PIN: 9999
Invalid pin
Please enter your PIN: 8888
Invalid pin
Please enter your PIN: 7777
Invalid pin

Account locked. The police is on its way.

# Part 1: Number counter. Write a program that counts numbers
Write a program that asks the user to input some parameters used to generate a range of numbers. The user should be prompted to enter a start value, an end value and a step value. The only required value is the end value; if the user hits enter without providing a number for the start or step, then the value 0 is used as the start and the default value of 1 is used for the step.
If the user enters an incorrect value (i.e. a string) or does not provide a required value, print a message indicating that the value is incorrect and prompt them again.
Once the values have been entered by the user, print the range to the screen.
Hello!
Enter a start value (Default: 0): 
Enter an end value: 10
Enter a step value (Default: 1):

The numbers are: 0 1 2 3 4 5 6 7 8 9 10



Hello!
Enter a start value (Default: 0): 2
Enter an end value: 10
Enter a step value (Default: 1): 2

The numbers are: 2 6 8 10


Hello!
Enter a start value (Default: 0): banana
Oops! Bad value! Please enter a number.

Enter a start value (Default: 0):
Enter an end value:
Oops! You must provide an end value.

Enter an end value: 10

...

