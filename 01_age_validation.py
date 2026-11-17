class AgeError(Exception):
    pass


age = int(input("Enter age: "))

try:
    if age < 18:
        raise AgeError("Age must be 18 or above")
    print("Valid age")
except AgeError as e:
    print(e)
