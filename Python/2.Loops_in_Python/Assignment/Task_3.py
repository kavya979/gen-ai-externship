'''Task 3 - Find the Factorial
Write a Python program to calculate the factorial of a number entered by the user.

Ask the user for a number.
Use a for loop to calculate the factorial.
Print the result in a friendly format.
For example:

Enter a number: 5
The factorial of 5 is 120.'''
n=int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("The factorial of", n , "is" , fact)