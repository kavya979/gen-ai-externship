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

print(f"Factorial is 5 is {factorial(5)}. The 6th Fibonacci number is {fibonacci(6)}.")

