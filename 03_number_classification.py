n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
