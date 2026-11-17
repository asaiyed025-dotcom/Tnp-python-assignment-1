from datetime import datetime

today = datetime.now()

print("Current date:", today.date())
print("Current time:", today.strftime("%H:%M:%S"))

dob = input("Enter DOB (YYYY-MM-DD): ")
dob = datetime.strptime(dob, "%Y-%m-%d")

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Age =", age)
