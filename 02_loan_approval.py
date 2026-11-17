salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))
age = int(input("Enter age: "))

if salary >= 30000 and credit >= 700 and age >= 21 and age <= 60:
    print("Approved")
elif salary >= 30000 or credit >= 700:
    print("Conditionally Approved")
else:
    print("Rejected")
