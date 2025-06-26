t=("Brave","Butterfly","Little Woman")
print("Favorite things:",t)
try:
    t[0]="Rapunzel"
except TypeError:
    print("Oops! Tuples cannot be changed.")
print("Length of tuple:",len(t))