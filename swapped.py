# Davis Arita
# September 12, 2022
# CS 131 Exercise 3 Part D
# swaps the first and last characters of a given string

string = input("Enter a string: ")
start = string[0]
end = string[-1]
swapped = end + string[1:-1] + start
print(swapped)