name = input("Your name: ")
age = int(input("Your age: "))
if age >= 18:
    print(f"{name}, you can vote!")
else:
    print(f"{name}, you are {18-age} years from voting.")
