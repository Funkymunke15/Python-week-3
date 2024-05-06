# Davis Arita
# September 14, 2022
# CS 131 In Class Lab 3B exercise 1
# Formatting a phone number

phoneNumber = input("The phone number is: ")

phoneNumber = "("+phoneNumber[:3]+") "+phoneNumber[3:6]+"-"+phoneNumber[6:]
print("The formatted number is: ", phoneNumber)
