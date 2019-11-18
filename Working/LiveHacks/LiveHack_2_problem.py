'''
-------------------------------------------------------------------------------
Name:		LiveHack_2_problem.py
Purpose:	Determine which type of triangle is which 

Author:	Sedighi.R

Created:	date in 18/11/2019
------------------------------------------------------------------------------
'''

# get the angles
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

#compute the type of triangle
if (angle1 == 60) and (angle2 == 60) and (angle3 == 60):
    print("A triangle with angles " + str(angle1) + ", " + str(angle2) + 
    ", and " + str(angle3) + " forms an Equilateral triangle.") 
elif (angle1+angle2+angle3 == 180) and (angle1 == angle2 or angle2== angle3 or angle1 == angle3):
    print("A triangle with angles " + str(angle1) + ", " + str(angle2) + 
    ", and " + str(angle3) + " forms an Isosceles triangle.") 
elif angle1+angle2+angle3 == 180:
     print("A triangle with angles " + str(angle1) + ", " + str(angle2) + 
    ", and " + str(angle3) + " forms an Scalene triangle.")
else:
    print("Error, the angles do not form a triangle.")
