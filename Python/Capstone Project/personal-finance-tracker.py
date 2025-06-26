'''
Step 1: Set up the project
Create a Python file named finance_tracker.py.

Print a welcome message when the program starts.

Expected Output:

Welcome to the Personal Finance Tracker!
Step 2: Add expenses
Use a loop to repeatedly ask the user to enter:

Expense description (string)

Category (string)

Amount (float)

Store each expense as a tuple: (description, amount)

Use a dictionary to organize expenses by category.

Expected Output (user input shown in brackets):

Enter expense description: [Lunch]
Enter category: [Food]
Enter amount: [12.5]
Expense added successfully.
Step 3: View all expenses
Define a function view_expenses(data) that prints all categories and their expenses.

Expected Output:

Category: Food
  - Lunch: $12.5
Step 4: View summary by category
Define a function view_summary(data) that shows the total amount spent per category.

Expected Output:

Summary:
Food: $45.75
Transport: $30.00
Step 5: Handle exceptions
Use try-except blocks to handle:

Non-numeric input for amounts

Empty inputs

Unexpected errors

Expected Output (for invalid input):

Enter amount: [abc]
Invalid amount. Please enter a number.
Step 6: Organize your code
Use functions to organize:

Adding an expense

Viewing expenses

Viewing summary

Menu logic

 

Step 7: Exit option
Allow users to exit the program using a menu-driven approach.

Expected Output:

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: [4]
Goodbye!
'''