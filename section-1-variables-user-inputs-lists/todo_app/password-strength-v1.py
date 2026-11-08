password = input("Enter new password: ")

result = [False, False, False]
if len(password) >= 8:
    result[0] = True

for x in password:
    if x.isdigit():
        result[1] = True
    elif x.isupper():
        result[2] = True

if all(result):
    print("Strong password")
else :
    print("Weak password")


