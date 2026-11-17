m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if m1 < 33 or m2 < 33 or m3 < 33 or m4 < 33 or m5 < 33:
    print("Result: Fail")
else:
    print("Result: Pass")

    if percentage >= 60:
        print("Division: First")
    elif percentage >= 50:
        print("Division: Second")
    elif percentage >= 40:
        print("Division: Third")
    else:
        print("Division: Fail")

print("Percentage =", percentage)
