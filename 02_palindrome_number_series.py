start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    temp = n
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if n == reverse:
        print(n, end=" ")
