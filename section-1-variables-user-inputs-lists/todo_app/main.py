user_prompt = "Enter a todo: "
todo = input(user_prompt)
print(todo)
todos = [ todo ]
length = len(todo)
print("The length of the todo: ", length)
print(f"You have {len(todos)} todos", )
print(type(todos))
