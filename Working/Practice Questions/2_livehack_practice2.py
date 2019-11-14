'''
-------------------------------------------------------------------------------
Name:		2_livehack_practice_solution2.py
Purpose:	compute the destination of a student based on marks and earnings

Author:	Sedighi.R

Created:	date in 11/08/2019
------------------------------------------------------------------------------
'''

# get marks, earnings
marks = float(input("Enter your mark: "))
earnings = float(input("Enter your earnings: "))

#compute and show destination
if marks >= 80 and earnings >= 500:
    print("You get to go to Europe.")
elif marks >= 80:
    print("You get to go to California.")
else:
    print("You stay home :(")
