password = "Secure3p@ss"
password_length = len(password)

if len(password) < 6:
    strength ="week"

elif len(password) <= 10:
    strength = "medium"

else:
    strength = "strong"

print("password strength is :", strength)