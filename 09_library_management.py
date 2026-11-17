library = {
    "Python": 3,
    "Java": 2,
    "DBMS": 4
}

while True:
    print("\n1. Show books")
    print("2. Search book")
    print("3. Issue book")
    print("4. Return book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for book, quantity in library.items():
            print(book, ":", quantity)

    elif choice == "2":
        book = input("Enter book name: ")
        if book in library:
            print("Available:", library[book])
        else:
            print("Book not found")

    elif choice == "3":
        book = input("Enter book name: ")
        if book in library and library[book] > 0:
            library[book] -= 1
            print("Book issued")
        else:
            print("Book not available")

    elif choice == "4":
        book = input("Enter book name: ")
        if book in library:
            library[book] += 1
        else:
            library[book] = 1
        print("Book returned")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
