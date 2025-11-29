class Student:
   def __init__(self, id, name, dob):
      self.__id = id
      self.__name = name
      self.__dob = dob
   def get_name(self):
      return self.__name

class Course:
   def __init__(self, id, name, list_students, list_marks):
      self.__id = id
      self.__name = name
      self.__list_students = list_students
      self.__list_marks = list_marks
   def get_mark(self, student_index):
      return self.__list_marks[student_index]
   def get_name(self):
      return self.__name

class Class:
   def __init__(self, list_students, list_courses):
      self.__list_students = list_students
      self.__list_courses = list_courses
   def list_students(self):
      for i in range(len(self.__list_students)):
         print(self.__list_students[i].get_name())
   def list_courses(self):
      for i in range(len(self.__list_courses)):
         print(self.__list_courses[i].get_name())
   def get_all_marks(self):
      message = ""
      for i in range(len(self.__list_students)):
         for j in range(len(self.__list_courses)):
            message += f"{self.__list_courses[j].get_name()} mark of {self.__list_students[i].get_name()} is {self.__list_courses[j].get_mark(i)}\n"
      print(message)

s1 = Student("1", "nam", "12/07/2006")
s2 = Student("2", "bac", "12/08/2006")
students = [s1, s2]
c1_marks = [8, 9]
c2_marks = [7, 8]
c1 = Course("1", "math", students, c1_marks)
c2 = Course("2", "english", students, c2_marks)
courses = [c1, c2]
cl = Class(students, courses)
cl.list_students()
cl.list_courses()
cl.get_all_marks()
