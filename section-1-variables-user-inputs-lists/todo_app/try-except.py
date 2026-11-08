print("Welcome to the try-except")

while True:
    user_action = input("Enter a number: ")
    if user_action == "exit":
        break

    try:
        number = int(user_action)
        print(number)
    except ValueError:
        print("Invalid number")
