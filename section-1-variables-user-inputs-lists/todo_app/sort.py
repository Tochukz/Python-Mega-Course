waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
for i, name in enumerate(waiting_list):
    print(f"{i+1}.{name.capitalize()}")