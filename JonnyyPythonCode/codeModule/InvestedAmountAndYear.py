amount = int(input("Enter the amount you want ot invest: "))
years = int(input("Enter the number of year: "))
rate = 0.05
returnOfInvestment = amount * rate
while years in range(1, years + 1):
    futureInterest = amount * returnOfInvestment
    amount = futureInterest
    print(f"Year {years} return investment is {futureInterest}")
