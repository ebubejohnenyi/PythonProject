userFirstName = input("Enter your name to get the value: ")
print(ord(userFirstName))
userSecondName = input("Enter second name to get the value: ")
print(ord(userSecondName))

if userFirstName > userSecondName:
    print("The First Person is the highest.")
elif userSecondName > userFirstName:
    print("The Second Person is the highest")