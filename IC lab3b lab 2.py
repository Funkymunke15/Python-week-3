# Davis Arita
# September 14, 2022
# CS 131 In Class Lab 3B exercise 2
# Swapping the middle two characters of a string of even length

string = input("Enter a string of an even length: ")
indexOfFirstMid = len(string)//2-1
indexOfSecondMid = len(string)//2

newString = string[:indexOfFirstMid] + string[indexOfSecondMid] +\
            string[indexOfFirstMid] + string[indexOfSecondMid+1:]


print(newString)
