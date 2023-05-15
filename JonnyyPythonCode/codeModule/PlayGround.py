# list_Name = 10
# names = []
# for index in range (list_Name):
#     userName = input("Enter your name: ")
#     if len(userName) > 0 and len(userName) <= 10:
#         names.append(userName)
#     if userName == 0:
#         print("Get this shit outta my face")
# print(names)


# def discount_receive():
#         userInput = float(input("Enter your Price: "))
#         if 20_000 < userInput < 50_000:
#             secondDiscount = userInput * 0.20
#             print("You've been given 20% discount and your new price is: ", secondDiscount)
#         elif 1 < userInput <= 20_000:
#             firstDiscount = userInput * 0.10
#             print("You've been given 10% discount and your new prince is: ", firstDiscount)
#         elif userInput > 50_000:
#             thirdDiscount = userInput * 0.30
#             print("You've been given 30% discount: ", thirdDiscount)
#
#
# discount_receive()

guess_Number = 4
userNumber = int(input("Enter a number from (1 - 5): "))
while userNumber != 4:
    userInput = int(input("Try again.! Enter a number: "))
    if userInput == 4:
        print("This is a lucky number")
        break
print("This is a lucky number ")