# This version of the program uses the match-case syntax
file = open("todos.txt", "r")
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()
    match user_action:
        case "add":
            todo = input("Enter todo: ") + "\n"
            todos.append(todo)
        case "show" | "display":
            for i, todo in enumerate(todos):
                print(f"{i+1}) {todo.strip('\n')}")
        case "edit":
            number = input("Enter todo number to edit: ")
            todo = input("Enter update: ") + "\n"
            todos[int(number) - 1] = todo
        case "complete":
            number = input("Enter todo number to complete: ")
            index = int(number) - 1
            todo = todos[index].strip('\n')
            todos.pop(index)
            print(f"'{todo}' has been removed from todo list!")
        case "exit":
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            break
        case _:
            print("Invalid input")

print("Bye!")
