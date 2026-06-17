import string
hasUpper = False
hasLower = False
hasDigit = False
hasSymbol = False

password = input("Enter your password: ")
score = 0

if len(password) >= 8:
    score += 1
for char in password:
    if char.isupper():
        hasUpper = True
    if char.islower():
        hasLower = True
    if char.isdigit():
        hasDigit = True
    if char in string.punctuation:
        hasSymbol = True
    if hasUpper and hasLower and hasDigit and hasSymbol:
        break
if hasUpper:
    score += 1
if hasLower:
    score += 1
if hasDigit:
    score += 1
if hasSymbol:
    score += 1

if score <= 2:
    print("Yor password strength is weak")
elif score <= 4:
    print("Yor password strength is medium")
else:
    print("Yor password strength is strong")



