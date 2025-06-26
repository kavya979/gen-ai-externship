import random
number_to_guess = random.randint(1, 100)
n=0
x=0
while (number_to_guess != n):
    if x==10:
        x=11
        break
    x+=1
    n =int(input("Guess the number (between 1 and 100): "))
    if number_to_guess > n:
        print(n,"Too low! Try again.")
    elif number_to_guess < n:
        print(n,"Too high! Try again.")
if x>10:
    print("Game over! Better luck next time!")
else:
    print(number_to_guess,"Congratulations! You guessed it in",x,"attempts!")

