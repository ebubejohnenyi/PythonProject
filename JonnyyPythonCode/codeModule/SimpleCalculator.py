import operator
from operator import sub, add, mul, truediv

add, sub, mul, truediv


def SimpleCalculator():
    firstUserNumber = input("Enter a number: ")
    secondUserNumber = input("Enter another number: ")
    thirdOperator = input("Enter any Operator (* or - or + or /): ")
    if thirdOperator == '+':
        print(f'{firstUserNumber + secondUserNumber}')
    elif thirdOperator == '-':
        print(f'{firstUserNumber - secondUserNumber}')
    elif thirdOperator == '//':
        print(f'{firstUserNumber // secondUserNumber}')
    elif thirdOperator == '*':
        print(f'{firstUserNumber * secondUserNumber}')


SimpleCalculator()
