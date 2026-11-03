# List Comprehension in Python is  like map() in JavaScript
# A List Comprehension can create a new list by modifying an existing list
numbers = [1, 2, 3, 4, 5]
multiples_of_5 = [ x * 5 for x in numbers]
print(multiples_of_5)


names = ['james brown', 'kelvin hart', 'peter packer']
title_names = [ name.title() for name in names]
print(title_names)

