s = input("Enter a string: ")

s = s.replace(" ", "").lower()

if s == s[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")
