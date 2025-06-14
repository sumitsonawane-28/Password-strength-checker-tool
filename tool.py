print("\n-----  welcome  -----\n")
print("--- To the password atrength checker ---")

password = input("\n--- Enter your password to check strength :")

strength = 0

if len(password) >= 8:
    strength += 1

if any(char.isupper() for char in password):
    strength += 1

if any(char.islower() for char in password):
    strength += 1

if any(char.isdigit() for char in password):
    strength += 1

if strength <= 2:
    print("\n--- password strength : weak\n")
elif (strength == 3 or strength == 4)  :
    print("\n--- password strength : medium\n")
else:
    print("\n--- password strength : strong\n")
