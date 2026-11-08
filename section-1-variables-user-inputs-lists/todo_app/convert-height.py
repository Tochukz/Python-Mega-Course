user_input = input("Enter feet and inches: ")

def convert_to_meters(feet_inches):
     args = feet_inches.split(" ")
     feet = float(args[0])
     inches = float(args[1])

     meters = feet * 0.3048 + inches * 0.0254
     return meters


result = convert_to_meters(user_input)
print(f"{result} meters")