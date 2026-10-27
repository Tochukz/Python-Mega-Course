todos = []
while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.lower().strip()
    match user_action:
        case "add":
            todo = input("Enter todo: ")
            todos.append(todo)
        case "show" | "display":
            for todo in todos:
                print(todo)
        case "exit":
            break
        case _:
            print("Invalid input")

print("Bye!")
