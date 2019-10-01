'''
-------------------------------------------------------------------------------
Name:		practice1.py
Purpose:	Convert fahrenheit to celsius

Author:	Sedighi.R

Created:	date in 01/10/2019
------------------------------------------------------------------------------
'''

# get fahrenheit from user
fahrenheit = float(input("Enter the fahrenheit: "))

# compute celsius from fahrenheit
celsius = (5/9)*(fahrenheit - 32)

# output celsius
print("The temperature in celsius is", celsius)
