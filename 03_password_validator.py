class PasswordError(Exception):
    pass


password = input("Enter password: ")

try:
    if len(password) < 8:
        raise PasswordError("Password must have at least 8 characters")

    if not any(ch.isupper() for ch in password):
        raise PasswordError("Password must contain an uppercase letter")

    if not any(ch.isdigit() for ch in password):
        raise PasswordError("Password must contain a number")

    print("Valid password")

except PasswordError as e:
    print("Invalid password:", e)
