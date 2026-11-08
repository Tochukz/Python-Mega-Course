file = open("todos.txt", "r")
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, show, edit, complete, help or exit: ")
    user_action = user_action.strip()

    if user_action.startswith(("add", "new")):
        todo = user_action[4:]
        todos.append(todo + "\n")
    elif user_action.startswith("show"):
        for i, todo in enumerate(todos):
            print(f"{i+1}) {todo.strip('\n')}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todo = input(f"Enter update for {number}: ") + "\n"
            todos[int(number) - 1] = todo
        except ValueError:
            print("Invalid edit input!")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = int(number) - 1
            todo = todos[index].strip('\n')
            todos.pop(index)
            print(f"'{todo}' has been removed from todo list!")
        except ValueError:
            print("Invalid complete input!")
            continue
        except IndexError:
            print("Todo item number is out of range!")
            continue
    elif user_action.startswith("exit"):
        with open("todos.txt", "w") as file:
            file.writelines(todos)
        break
    elif user_action.startswith("help"):
      print("Example commands: ")
      print("  To add a new todo item: add Learning Python")
      print("  To show all todos item: show")
      print("  To edit todo item no1: edit 1")
      print("  To mark todo item no2 as completed: complete 2")
      print("  To end the program: exit")
    else:
        print("Invalid input!")

print("Bye!")
