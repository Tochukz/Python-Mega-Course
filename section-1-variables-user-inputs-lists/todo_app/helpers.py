def get_todos():
    file = open("todos.txt", "r")
    todos = file.readlines()
    file.close()
    return todos


def print_help():
    print("Example commands: ")
    print("  To add a new todo item: add Learning Python")
    print("  To show all todos item: show")
    print("  To edit todo item no1: edit 1")
    print("  To mark todo item no2 as completed: complete 2")
    print("  To end the program: exit")