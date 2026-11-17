subjects = (
    input("Enter subject 1: "),
    input("Enter subject 2: "),
    input("Enter subject 3: "),
    input("Enter subject 4: "),
    input("Enter subject 5: ")
)

print("Third subject:", subjects[2])
print("Total subjects:", len(subjects))

name = input("Enter subject to find index: ")

if name in subjects:
    print("Index:", subjects.index(name))
else:
    print("Subject not found")
