import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

def main():
    while True:
        try:
            n = int(input("Choose an operation: \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit \n"))
            if n<5:
                n1=int(input("Enter the first number: "))
                n2=int(input("Enter the second number: "))

                if n==1:
                    print(f"Sum of {n1} and {n2} gives {n1+n2}")
                elif n==2:
                    print(f"Difference of {n1} and {n2} gives {n1-n2}")
                elif n==3:
                    print(f"Product of {n1} and {n2} gives {n1*n2}")
                elif n==4:
                    try:
                        result = n1 / n2
                        print(f"Division of {n1} by {n2} is {result}")
                    except ZeroDivisionError as e:
                        print("Dividing by zero is not allowed.")
                        logging.error(f"ZeroDivisionError occurred: {e}")
            else:
                if n==5:
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
        except ValueError as e:
            print("Please enter numerical values")
            logging.error(f"ValueError occurred: {e}")


main()
