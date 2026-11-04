# Using the "with" context manager

with open('todos.txt', 'r') as file:
    todos = file.readlines()

print(todos)