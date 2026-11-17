correct_password = "python123"

for i in range(3):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break
    else:
        print("Wrong password")

else:
    print("Account blocked after 3 failed attempts")
