# This show how to use the 'or', 'and' and 'not' boolean operators
position = input("Enter your position: ").lower().strip()
if "staff" in position or "principal" in position:
    print("You are right where you are suppose to be")
elif  "senior" in position and "developer" in position:
    print("You need to move up")
elif "cto" not in position:
    print("How about being a CTO?")