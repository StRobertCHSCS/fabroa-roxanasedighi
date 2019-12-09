'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	determine number of days to travel 100km and the average of distance

Author:	Sedighi.R

Created:	date in 09/12/2019
------------------------------------------------------------------------------
'''

print("***** Welcome to the Distance Tracker ******")

# initialize counters
number_of_days = 0
daily_distance = 0
total_distance = 0

# get the distance user travelled each day and determine total
while total_distance < 100:
    daily_distance = int(input("Enter the distance travelled for the day:"))
    total_distance = total_distance + daily_distance
    number_of_days += 1

# compute the average
average = total_distance//number_of_days

# output number of days and the average
print("It took " + str(number_of_days) + " days to surpass 100km driven.")
print("The average distance driven per day is " + str(average) + " km.")