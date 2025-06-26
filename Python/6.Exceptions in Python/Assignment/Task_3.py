try:
    n1=int(input("Enter the first numbers: "))
    n2=int(input("Enter the second numbers: "))
    z=n1/n2
except ZeroDivisionError:
    print("Please enter a value greater than 0")
except ValueError:
    print("Please enter a numeric input")
else:
    print(f"The result is {z}.")
finally:
    print("This block always executes.")


