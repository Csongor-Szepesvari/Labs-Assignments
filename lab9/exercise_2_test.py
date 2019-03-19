import unittest
from exercise_2 import *
import random

	
def test_print_student():
	student = Student("ID_1", "Name_1", 100)
	print(str(student) == " - ID_1, Name_1, 100")

def test_is_greater_than():
	student_1 = Student("ID_1", "Name_1", 80)
	student_2 = Student("ID_2", "Name_2", 90)
	print(student_1.is_greater_than(student_2)==False)
	print(student_2.is_greater_than(student_1)==True)

def test_sort_students_in_and_out_of_order():
	student_1 = Student("ID_1", "Name_1", 60)
	student_2 = Student("ID_2", "Name_2", 80)
	student_3 = Student("ID_3", "Name_3", 50)

	students_input_list=[student_1,student_2,student_3]
	output = [ str(student) for student in sort_students(students_input_list)]

	students_sorted_list = [str(student_3),str(student_1),str(student_2)]
	print(output==students_sorted_list)

def test_sort_students_repeated_marks():
	student_1 = Student("ID_1", "Name_1", 60)
	student_2 = Student("ID_2", "Name_2", 80)
	student_3 = Student("ID_3", "Name_3", 50)
	student_4 = Student("ID_4", "Name_4", 50)

	students_input_list=[student_1,student_2,student_3, student_4]
	output = [ str(student) for student in sort_students(students_input_list)]

	students_sorted_list = [str(student_4), str(student_3) ,str(student_1),str(student_2)]
	print(output==students_sorted_list)
	
test_print_student()
test_is_greater_than()
test_sort_students_in_and_out_of_order()
test_sort_students_repeated_marks()
	
	


