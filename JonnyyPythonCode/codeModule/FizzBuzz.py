def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 ==0:
        return  "buzz"
print(fizzbuzz(15))
