file = open("todos.txt", "r")
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action or "new" in user_action:
        todo = user_action[4:]
        todos.append(todo + "\n")
    elif "show" in user_action:
        for i, todo in enumerate(todos):
            print(f"{i+1}) {todo.strip('\n')}")
    elif "edit" in user_action:
        number = int(user_action[5:])
        todo = input(f"Enter update for {number}: ") + "\n"
        todos[int(number) - 1] = todo
    elif "complete" in user_action:
        number = int(user_action[9:])
        index = int(number) - 1
        todo = todos[index].strip('\n')
        todos.pop(index)
        print(f"'{todo}' has been removed from todo list!")
    elif "exit" in user_action:
        with open("todos.txt", "w") as file:
            file.writelines(todos)
        break
    else:
        print("Invalid input!")

print("Bye!")
