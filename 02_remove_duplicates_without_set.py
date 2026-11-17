numbers = list(map(int, input("Enter list elements: ").split()))
new_list = []

for x in numbers:
    if x not in new_list:
        new_list.append(x)

print("List after removing duplicates:", new_list)
