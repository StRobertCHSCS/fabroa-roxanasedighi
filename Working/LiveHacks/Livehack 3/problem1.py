'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	computing the number of heating days if average is 
            below 15 degrees celcius

Author:	Sedighi.R

Created:	date in 09/12/2019
------------------------------------------------------------------------------
'''

print("******  Heating Days Tracker ******")

# get the number of days
number_of_days = int(input("Enter the number of days to track: "))

# initialize total
heating_days = 0

# compute the total temperature
for i in range(number_of_days):
    temp = int(input("Enter a temperature: "))
    heating_days = heating_days + number_of_days

print("There are " + str(heating_days) + " heating days.")