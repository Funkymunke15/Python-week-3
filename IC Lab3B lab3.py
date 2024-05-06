# Davis Arita
# September 14, 2022
# CS In class Lab 3B exercise 3
# helps a person decide whether to buy a hybrid car or not

costOfNewCar = int(input("Enter the cost of the car: "))
milesPerYear = int(input("How many miles will you drive each ear?"))
gasPrice = int(input("Enter the price of gas per gallon: "))
mpgEfficiency = int(input("Enter the fuel efficiency in mpg: "))
resaleAfter5Years = int(input("How much can you sell the car for after 5 years? "))

costOfOwnership = costOfNewCar + 5*milesPerYear*gasPrice/mpgEfficiency - resaleAfter5Years

print("The total cost of ownership is $%.2f" % costOfOwnership)
