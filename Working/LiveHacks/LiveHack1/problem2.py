'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	determine number of chickens for each person in Mr.Fabroa's class

Author:	Sedighi.R

Created:	date in 02/10/2019
------------------------------------------------------------------------------
'''

# get number of students and chickens from user
students = int(input("Enter the number of students: "))
chickens = int(input("Enter the number of chickens: "))

# compute number of chickens the class get
each_student = chickens//students
Mr_Fabroa = chickens % students

# output number of chickens for each person
print("Each student will get", each_student, "pieces of chicken.")
print("Mr.Fabroa will get", Mr_Fabroa, "pieces of chicken.")
