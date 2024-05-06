# Davis Arita
# September 12, 2022
# CS 131 Exercise 3 Part C
# Takes user input for current time and an amount to wait for an alarm
# and calculates when the alarm should go off

curTime = int(input("What is the current time (in military format)?"))
alarm = int(input("After how many hours should the alarm go off?"))

rawTime = curTime + alarm
actualTime = (rawTime + 24) % 24

print("The alarm should go off at %d" % actualTime)