# Davis Arita
# September 12, 2022
# CS 131 Exercise 3 Part E
# Duplicates the first half and second half of a string
string = input("Enter a string: ")
firstHalf = string[:len(string)//2]
secondHalf = string[len(string)//2:]

# print(firstHalf, secondHalf)

print(firstHalf*2+secondHalf*2)
