try:
    n=int(input("Enter a number: "))
    x=100/n
    print(x)
except ZeroDivisionError:
    print("Please enter a value greater than 0")
except ValueError:
    print("Please enter a numeric input")