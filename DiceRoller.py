#!/usr/bin/env python
#Written and uploaded on 10/26/2017
#created in an afternoon by Leanne Vermillion
#project solution to a project posted on projecteuler.net
import random
import math

def fourside():
	four = random.randint(1, 4)
	#print four
	return four

def sixside(four):
	six = 0
	for i in range(four):
		rolls = random.randint(1, 6)
		six += rolls
	#print six
	return six

def eightside(six):
	eight = 0
	for i in range(six):
		rolls = random.randint(1, 8)
		eight += rolls
	#print eight
	return eight

def tenside(eight):
	ten = 0
	for i in range(eight):
		rolls = random.randint(1, 10)
		ten += rolls
	#print ten
	return ten

def twelveside(ten):
	twelve = 0
	for i in range(ten):
		rolls = random.randint(1, 12)
		twelve += rolls
	#print twelve
	return twelve

def twentyside(twelve):
	twenty = 0 
	for i in range(twelve):
		rolls = random.randint(1, 20)
		twenty += rolls
	return twenty

def run(inputRolls):
	highVal = 0
	lowVal = 0
	runTotal = 0
	for i in range(inputRolls):
		four = fourside()
		six = sixside(four)
		eight = eightside(six)
		ten = tenside(eight)
		twelve = twelveside(ten)
		twenty = twentyside(twelve)

		if (highVal < twenty):
			highVal = twenty
			#print highVal
		if (lowVal == 0 or lowVal > twenty):
			lowVal = twenty
			#print lowVal
		if (runTotal == 0):
			runTotal = twenty
		else:
			runTotal += twenty
			#print runTotal
	runAve = runTotal/inputRolls
	print "The Average for" , inputRolls , "rolls is" , runAve
	print "The lowest value you got was" , lowVal
	print "The highest value you got was" , highVal

print "This application rolls a 4 sided die and then with"
print  "the results of that roll will roll that many 6 sided dice, "
print "then again with 8 sided, 10 sided, 12 sided and 20 sided. "
print "Try this multiple times and see what your average and "
print "highest and lowest values are."

inputVal = input('Enter a number of times to roll the dice: ')
try:
    inputRolls = int(inputVal)
    run(inputRolls)
except ValueError:
    print("Invalid number")




