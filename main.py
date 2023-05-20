"""
TYPES

string   a string is some text that you can print or save to file 
int      is a number, that you can add, take away, divide, multiply you can not print an int
datetime you can add two datetimes,  you can not pritn datetime




"""

import datetime as dt 


print("Welcome to Weight Tracker")



current_date = dt.date.today()


print("Today's Day: " + str(current_date))


print("Please tell me your weight in kilograms.")


weight = input('please enter a number in kg: ')

if(type(weight) != int):
	print("Sorry you did not enter a number")
	exit()

print("Your weight is:" + str(weight) + ' kg') 
