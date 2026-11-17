numbers = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter k: "))
side = input("Enter left or right: ").lower()

k = k % len(numbers)

if side == "left":
    numbers = numbers[k:] + numbers[:k]
elif side == "right":
    numbers = numbers[-k:] + numbers[:-k]

print("Rotated list:", numbers)
