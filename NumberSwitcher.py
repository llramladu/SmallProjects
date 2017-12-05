#!/usr/bin/env python
#Written and uploaded on 12/4/2017
#created in an afternoon by Leanne Vermillion
#Similar to a project posted on projecteuler.net Problem 168
import math

def run(inputNumber):

	for n in range(11110, inputNumber+1):
		currentNumber = n
		currentString = str(currentNumber)	
		#print currentString
		lastNumber = currentString[-1:]
		newString = currentString[:-1]
		#print newString
		newString = lastNumber + newString
		#print newString
		newNumber = int(newString)
		#print newNumber
		if newNumber % currentNumber == 0:
			if newNumber != currentNumber:
				print "The number " + currentString + " is a factor of " + newString + "."
		#elif newNumber == currentNumber:
			#The numbers are equal so technically a factor but not very interesting to look at
			#print "The number " + currentString + " is a factor of " + newString + ", because they are the same."
		#elif currentNumber % newNumber == 0:
			#Another possible way of seeing if two numbers are factors of each other.
			#Uses int for number because it'll print 0 at the beginning if the string is used.
			#print "The number" , newNumber , "is a factor of " + currentString +"."

print "This application takes a number from a user."
print "Then each 5 digit number up to the entered value is tested."
print "The last number is removed and added to the front so 142857 would become 7142857."
print "If the original number is a factor of the new number that information is printed to the screen."
print "With large numbers this make take some time."

inputVal = input('Enter a number between 15000 and 9000000000000000000: ')
try:
	inputNumber = int(inputVal)
	if inputVal < 15000 or inputVal > 9000000000000000000:
		print("Invalid number")
	else:
		run(inputNumber)
except ValueError:
	print("Invalid number")

