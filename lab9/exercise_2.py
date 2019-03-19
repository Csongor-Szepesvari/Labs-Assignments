# Define the Student class
class Student():
  
  # Initialize the object properties
  def __init__(self, ID, name, mark):
    self.__ID = ID
    self.__name = name
    self.__mark = mark

  # Print the object as an string
  def __str__(self):
      return ' - {}, {}, {}'.format(self.__ID, self.__name, self.__mark)

  # Check if the mark of the input student is greater than the student object
  # The output is either True or False
  def is_greater_than(self, another_student):
    return self.__mark > another_student.__mark
    
  def __gt__(self, o):
    return self.__mark > o.__mark
  
  def __lt__(self, o):
    return self.__mark < o.__mark
  
  def __eq__(self, o):
    return self.__mark == o.__mark

# Sort the student_list
# The output is the sorted list of students
def sort_students(student_list):
  return merge_sort(student_list)

def merge_sort(aList):
  if len(aList)>1:
    m = len(aList)//2
    left = merge_sort(aList[:m])
    right = merge_sort(aList[m:])
    return merge(left, right)
  else:
    return aList

def merge(left, right):
  toRet = []
  l = 0
  r = 0
  for i in range(len(left)+len(right)):
    if left[l] < right[r]:
      toRet.append(left[l])
      l += 1
    else:
      toRet.append(right[r])
      r += 1
    if l == len(left):
      toRet += right[r:]
      break
    elif r == len(right):
      toRet += left[l:]
      break
  return toRet
    
  
  

if  __name__== "__main__":
  # Read the data
  students_file = open('student_list.txt', 'rt')
  students_data = students_file.readlines()
  student_list = []
  for student in students_data:
    # Create a student object
    fields = student.split(', ')
    ID = fields[0]
    name = fields[1]
    mark = fields[2]
    student_list.append(Student(ID, name, int(mark)))

  # Print the original data
  print('Original data:')
  for student in student_list:
    print(student)

  # Sort the students
  sorted_students = sort_students(student_list)

  # Print the sorted data
  print('Sorted data:')
  for student in sorted_students:
    print(student)
    
  a = [5,3,7,1,10]
  print(merge_sort(a))