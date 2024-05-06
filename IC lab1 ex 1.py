# Davis Arita
# September 12, 2022
# CS 131 Lecture 3A Exercise 1
# calculates change in dollars, quarters, dimes, nickels, and pennies

my_money = 521
owe = 41

change = my_money - owe
# calculating dollars and change
changeDollar = change//100
change = change % 100
# calculating number of quarters and change
changeQuarter = change//25
change = change % 25
# calculating number of dimes and change
changeDime = change//10
change = change % 10
# calculating number of nickels
changeNickel = change//5
# remainder after number of nickels is pennies
changePenny = change % 5

print("Your change is %d dollars, %d quarters, %d dimes, %d nickels, and %d pennies "
      % (changeDollar, changeQuarter, changeDime, changeNickel, changePenny))
