from utils.parsers import parse_input, convert_to_meters

user_input = input("Enter feet and inches: ")
# feet_inches = parse_input(user_input)
# result = convert_to_meters(feet_inches[0], feet_inches[1])

ft, inh = parse_input(user_input)
result = convert_to_meters(ft, inh)

print(f"{result} meters")