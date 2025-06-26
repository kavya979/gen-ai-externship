# Recieve the age input as float (to be more friendly with decimal numbers)
age = float(input("How old are you? "))
# Check if the age is 18 or older
if age>=18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
# Condition if the age is younger than 18 (if the number is equal to or greater than 18, it has to be lesser than 18)
else:
    print(f"Oops! You're not eligible yet. But hey, only {int(18 - age)} more years to go!")