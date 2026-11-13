def parse_input(feet_inches_input):
     args = feet_inches_input.split(" ")
     feet = float(args[0])
     inches = float(args[1])
     return feet, inches


def convert_to_meters(feet, inches):
     meters = feet * 0.3048 + inches * 0.0254
     return meters
