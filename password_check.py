
import getpass
import string

# Step 1: Get password input
password = getpass.getpass(
    "Enter a test password (input is hidden): "
)

# Step 2: Initialize score and suggestions
score = 0
suggestions = []

# Step 3: Check password length
if len(password) >= 12:
    score += 1
else:
    suggestions.append("Use at least 12 characters.")

# Step 4: Check lowercase letters
if any(ch.islower() for ch in password):
    score += 1
else:
    suggestions.append("Add lowercase letters.")

# Step 5: Check uppercase letters
if any(ch.isupper() for ch in password):
    score += 1
else:
    suggestions.append("Add uppercase letters.")

# Step 6: Check numbers
if any(ch.isdigit() for ch in password):
    score += 1
else:
    suggestions.append("Add numbers.")

# Step 7: Check special characters
if any(ch in string.punctuation for ch in password):
    score += 1
else:
    suggestions.append("Add special symbols like !, @, or #.")

# Step 8: Display the result
print("\n--- Password Security Report ---")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Moderate")
else:
    print("Strength: Strong")

# Step 9: Display suggestions
if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Good! All five checks are satisfied.")

print("\nNote: This is a basic educational checker.")
print("Never enter your real password into an unfamiliar program.")
