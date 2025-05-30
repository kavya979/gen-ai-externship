'''
Task 3 - Conditional Statements: The Number Checker
Now for the real challenge: let's make your code think!

Write a program that takes a number from the user and tells them whether it's positive, negative, or zero.
Here's how it should work:

Ask the user to enter a number (use the input() function).
Use if, elif, and else statements to check:
If the number is greater than 0, print: "This number is positive. Awesome!"
If the number is less than 0, print: "This number is negative. Better luck next time!"
If the number is exactly 0, print: "Zero it is. A perfect balance!"

'''
n = float(input("enter a number:"))
if n>0:
    print("This number is positive. Awesome!")
elif 0>n:
    print("This number is negative. Better luck next time!")
elif n==0:
    print("Zero it is. A perfect balance!")