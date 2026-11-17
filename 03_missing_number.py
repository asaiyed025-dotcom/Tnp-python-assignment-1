numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter n: "))

total = n * (n + 1) // 2
missing = total - sum(numbers)

print("Missing number =", missing)
