import string


password = input("Enter password: ")
score = 0

if len(password) >= 8:
    score += 1

has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break
if has_upper:
    score += 1

has_number = False
for char in password:
    if char.isdigit():
        has_number = True
        break
if has_number:
    score += 1

has_special = False
for char in password:
    if char in string.punctuation:
        has_special = True
        break
if has_special:
    score += 1

print("\nScore:", score, "/ 4")

if score == 4:
    print("Strength: Strong")
elif score == 3:
    print("Strength: Medium")
else:
    print("Strength: Weak")
