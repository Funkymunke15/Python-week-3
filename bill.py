# Davis Arita
# September 12, 2022
# CS 131 Exercise 3 Part A
# Splits a bill to pay between a number of people
TIP = 15
partySize = 4
billAmount = 200
tipAmount = ((TIP/100)*billAmount)
perPerson = (((TIP/100)*billAmount)+billAmount)/partySize
print("The bill is $%.2f" % billAmount)
print("The tip is %d" % TIP)
print("Each person has to pay $%.2f" % perPerson)
