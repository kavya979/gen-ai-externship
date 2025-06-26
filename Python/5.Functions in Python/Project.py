import turtle
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
def fibonacci(k):
    if k ==0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k-1)+ fibonacci(k-2)

def fractal_pattern():
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.color("green")
    pen.left(90)
    pen.speed("fastest")

    def draw_tree(branch_length):
        if branch_length < 10:
            return
        pen.forward(branch_length)
        pen.right(30)
        draw_tree(branch_length - 15)
        pen.left(60)
        draw_tree(branch_length - 15)
        pen.right(30)
        pen.backward(branch_length)

    pen.penup()
    pen.goto(0, -150)
    pen.pendown()
    draw_tree(60)

    print("A fractal tree drawing!")
    screen.exitonclick()


def main():
    while True:
        n = int(input("Enter the Menu option: \n1. Calculate Factorial \n2. Find Fibonacci \n3. Draw a Recursive Fractal \n4.Exit \n"))
        if n==1:
            n=int(input("Enter a number:"))
            print(f"Factorial is {n} is {factorial(n)}.")
        elif n==2:
            n=int(input("Enter a number:"))
            print(f"The {n}th Fibonacci number is {fibonacci(n)}.")
        elif n==3:
            fractal_pattern()
        elif n==4:
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
main()