password = input("Enter new password: ")

result = {"validLen": len(password) >= 8, "hasDigit": False, "hasUpperCase": False}

for x in password:
    if x.isdigit():
        result["hasDigit"] = True
    elif x.isupper():
        result["hasUpperCase"] = True

if all(result.values()):
    print("Strong password")
else :
    print("Weak password")


