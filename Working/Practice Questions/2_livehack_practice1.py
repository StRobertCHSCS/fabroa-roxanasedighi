'''
-------------------------------------------------------------------------------
Name:		1_livehack_practice_solution1.py
Purpose:	Determine if a triangle is a right angle triangle

Author:	Sedighi.R

Created:	date in 11/08/2019
------------------------------------------------------------------------------
'''

#get side lengths
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

#compute squares
sq1 = side1**2
sq2 = side2**2
sq3 = side3**2

#determine if right triangle
if (sq1+sq2 == sq3) or (sq1+sq3 == sq2) or (sq2+sq3 == sq1):
    print("A triangle with lengths " + str(side1) + ", " + 
    str(side2) + ", and " + str(side3) + " forms a right-angled triangle.")
else:
    print("A triangle with lengths " + str(side1) + ", " + 
    str(side2) + ", and " + str(side3) + " does not form a right-angled triangle.")