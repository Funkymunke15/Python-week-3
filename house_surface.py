# Davis Arita
# September 12, 2022
# CS 131 Exercise 3 Part B
# calculates the surface area of a house to paint

houseWidth = 23
houseLength = 45
houseHeight = 9.5
numWindows = 12
windowWidth = 3
windowHeight = 3.5
numDoors = 4
doorWidth = 3
doorHeight = 7.5

totalWinArea = numWindows * (windowHeight*windowWidth)
totalDoorArea = numDoors * (doorHeight * doorWidth)
totalArea = (2*houseHeight*houseLength) + (2*houseWidth*houseHeight) - totalDoorArea - totalWinArea

print("The surface area to be painted of a house is %.2f sqft." % totalArea)
