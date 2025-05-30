'''
Step 1: Ask the User's Age
Your program should start by asking the user:

age = int(input("How old are you? "))
Make sure you convert the input into an integer so you can use it in calculations later.

Step 2: Decide the Eligibility
Use a conditional statement to check if the age is 18 or older. Here's the logic:

If the user's age is 18 or above, display a warm message like:
"Congratulations! You are eligible to vote. Go make a difference!"
If the user's age is less than 18, calculate how many years they have to wait. Display a friendly message like:
"Oops! You're not eligible yet. But hey, only X more years to go!"
Step 3: Test with Different Ages
Here's an example of how your program should behave:

Example Run 1:

How old are you? 16
Oops! You're not eligible yet. But hey, only 2 more years to go!
Example Run 2:

How old are you? 20
Congratulations! You are eligible to vote. Go make a difference!
Step 4: Polish It Up
Make sure your program is friendly, clear, and fun! Add comments to explain what your code is doing and maybe throw in a fun line or emoji for extra flair.
'''
# Recieve the age input as float (to be more friendly with decimal numbers)
age = float(input("How old are you? "))
# Check if the age is 18 or older
if age>=18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
# Condition if the age is younger than 18 (if the number is equal to or greater than 18, it has to be lesser than 18)
else:
    print(f"Oops! You're not eligible yet. But hey, only {int(18 - age)} more years to go!")