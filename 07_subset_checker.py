a = set(map(int, input("Enter first set: ").split()))
b = set(map(int, input("Enter second set: ").split()))

if a.issubset(b):
    print("First set is a subset of second set")
else:
    print("First set is not a subset of second set")
