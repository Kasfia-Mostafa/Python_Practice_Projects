print("Character Type Checker")

char = input("Enter a single character: ")

if char.isalpha():
    print("This a letter.")
elif char.isdigit():
    print("This is a digit")
else:
    print("This is a special character")
