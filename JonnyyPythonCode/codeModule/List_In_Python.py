list_of_numbers = list(range(1,21))
print (list_of_numbers)

# odd_not = int(input("Enter a number: "))
# print (odd_not)
# if (odd_not % 2)==0:
#     print ("This is an even number")
# else: print ("This is an odd number")

odd_numbers = list_of_numbers[::2]
print (odd_numbers)

mytuple = (i for i in range (500))
tuple_count = tuple(mytuple)
tuple_count = tuple_count[0:5]
print(tuple_count)