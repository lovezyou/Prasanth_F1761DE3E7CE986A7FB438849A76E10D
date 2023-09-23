


class Student:

	def __init__(self, name, roll_number, cgpa):
		self.name = name
		self.roll_number = roll_number
		self.cgpa = cgpa



def sort_students(student_list):
	#sort the list of students in descending order of CGPA
	sorted_students = sorted(student_list,
				key=lambda student: student.cgpa,
				reverse=True)
	return sorted_students  #return the list after sorted
	
	

# Example usage:
# students list
students = [
	Student("Adhi","A123", 8.8),
	Student("Faiyas","A124", 8.9),
	Student("Imiliya","A125", 9.8),
	Student("Parhti", "A126", 9.9),
	Student("Sivram", "A127", 9.5),
]

sorted_students = sort_students(students)

# Using for loop simultaneously sort the student list & Print the sorted list  of students
for student in sorted_students:
	print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
	
	
