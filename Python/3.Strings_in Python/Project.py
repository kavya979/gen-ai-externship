import string
n= input("Enter a password: ")
n_errors = []
error=["at least 8 characters","at least one uppercase letter","at least one lowercase letter","at least one digit","at least one special character (e.g., @, #, $)"]
score = 0
if len(n)>=8:
    score+=2
else:
    n_errors.append(error[0])
if any(char.isupper() for char in n):
    score+=2
else:
    n_errors.append(error[1])
if any(char.islower() for char in n):
    score+=2
else:
    n_errors.append(error[2])

if any(char.isdigit() for char in n):
    score+=2
else:
    n_errors.append(error[3])
special=string.punctuation
if any(char in special for char in n):
    score+=2
else:
    n_errors.append(error[4])
if not n_errors:
    print("Your password is strong! 💪")
else:
    print("your password needs" + "and".join(n_errors)+".")

print("Password Stength:", score)
if score == 10:
    print("💯 Excellent password!")
elif score >= 6:
    print("👍 Good, but could be stronger.")
else:
    print("⚠️ Weak password. Consider improving it.")
