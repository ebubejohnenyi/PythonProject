amount = int(input("Enter the amount you want ot invest: "))
years = int(input("Enter the number of year: "))
rate = 0.05
returnOfInvestment = amount * rate
for years in range(1, years + 1):
    print(years)