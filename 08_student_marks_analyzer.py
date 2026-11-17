marks = {
    "Aman": 78,
    "Riya": 91,
    "Rohit": 65,
    "Neha": 28,
    "Vikas": 42
}

topper = max(marks, key=marks.get)
average = sum(marks.values()) / len(marks)

print("Topper:", topper, marks[topper])
print("Average:", average)

print("Failed students:")
for name in marks:
    if marks[name] < 33:
        print(name)
