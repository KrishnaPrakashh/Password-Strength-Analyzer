
print("PASSWORD STRENGTH ANALYZER")
print("=" * 30)

password = input("Enter your password: ")

score = 0
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# Length Check
if len(password) >= 8:
    score += 2

# Uppercase Check
if any(char.isupper() for char in password):
    score += 1

# Lowercase Check
if any(char.islower() for char in password):
    score += 1

# Number Check
if any(char.isdigit() for char in password):
    score += 1

# Special Char Check
if any(char in special_chars for char in password):
    score += 2

# Strength 
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
elif score <= 6:
    strength = "Strong"
else:
    strength = "Very Strong"


print("Strength:", strength)

# Suggestions
print("\nSuggestions:")

has_suggestions = False

if len(password) < 8:
    print("- Increase length to at least 8 characters")
    has_suggestions = True

if not any(char.isupper() for char in password):
    print("- Add uppercase letters")
    has_suggestions = True

if not any(char.islower() for char in password):
    print("- Add lowercase letters")
    has_suggestions = True

if not any(char.isdigit() for char in password):
    print("- Add numbers")
    has_suggestions = True

if not any(char in special_chars for char in password):
    print("- Add special characters")
    has_suggestions = True

if not has_suggestions:
    print("- No suggestions. Your password looks good!")

# Common Password Check
try:
    with open("common.txt", "r") as file:
        common_passwords = file.read().splitlines()

    if password.lower() in common_passwords:
        print("\nWARNING: Common password detected!")
except FileNotFoundError:
    print("\ncommon.txt file not found.")