import string

print("\n-----  Welcome  -----\n")
print("--- To the password strength checker ---")

password = input("\n--- Enter your password to check strength: ")

strength = 0

if len(password) >= 8:
    strength += 1

if any(char.isupper() for char in password):
    strength += 1

if any(char.islower() for char in password):
    strength += 1

if any(char.isdigit() for char in password):
    strength += 1

if any(char in string.punctuation for char in password):
    strength += 1

if strength <= 2:
    print("\n\033[91m--- Password strength: Weak\033[0m\n")
elif strength <= 4:
    print("\n\033[93m--- Password strength: Medium\033[0m\n")
else:
    print("\n\033[92m--- Password strength: Strong\033[0m\n")
