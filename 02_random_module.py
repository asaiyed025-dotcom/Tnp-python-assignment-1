import random
import string

otp = random.randint(100000, 999999)

chars = string.ascii_letters + string.digits
password = ""

for i in range(8):
    password += random.choice(chars)

numbers = []

for i in range(5):
    numbers.append(random.randint(1, 100))

print("OTP =", otp)
print("Random password =", password)
print("Random list =", numbers)
