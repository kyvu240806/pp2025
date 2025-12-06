import math
import numpy as np

class Entity:
   def __init__(self):
      self.__id = ""
      self.__name = ""

   def input(self):
      self.__id = input("ID: ")
      self.__name = input("Name: ")

   def print(self):
      print("ID is ", self.__id)
      print("Name is ", self.__name)

   def getName(self):
      return self.__name

class Student(Entity):
   def __init__(self):
      super().__init__()
      self.__dob = ""
      self.__gpa = 0

   def input(self):
      super().input()
      self.__dob = input("DoB: ")

   def setGPA(self, gpa):
      self.__gpa = gpa

   def __lt__(self, other):
      return self.__gpa < other.__gpa

   def print(self):
      super().print()
      print("DoB is ", self.__dob)
      print("GPA is ", self.__gpa)

class Course(Entity):
   def __init__(self):
      super().__init__()
      self.__credits = 0

   def input(self):
      super().input()
      self.__credits = int(input("Number of credits: "))

   def getCredits(self):
      return self.__credits

class Mark: #not used
   def __init__(self):
      self.__studentID = 0
      self.__courseID = 0
      self.__mark = 0.0

   def input(self):
      self.__studentID = int(input("Student ID to get mark: "))
      self.__courseID = int(input("Course ID to get mark: "))
      self.__mark = float(input("Mark: "))

class School:
   def __init__(self):
      self.__students = []
      self.__courses = []
      self.__marks = [[]]

   def inputStudents(self):
      numStudents = int(input("Number of students: "))
      for i in range(numStudents):
         s = Student()
         s.input()
         self.__students.append(s)

   def inputCourses(self):
      numCourses = int(input("Number of courses: "))
      for i in range(numCourses):
         c = Course()
         c.input()
         self.__courses.append(c)

   def input(self):
      self.inputStudents()
      self.inputCourses()
      numStudents = len(self.__students)
      numCourses = len(self.__courses)
      self.__marks = [[0 for _ in range(numCourses)] for _ in range(numStudents)]

      for i in range(numStudents):
         for j in range(numCourses):
            mark = float(input(f"{self.__courses[j].getName()} mark of {self.__students[i].getName()}: "))
            #round the mark to 1-digit decimal
            roundedMark = math.floor(10*mark)/10
            self.__marks[i][j] = roundedMark

   def calGPA(self):
      #calculate the GPAs
      numStudents = len(self.__students)
      numCourses = len(self.__courses)
      credits = [0 for _ in range(numCourses)]

      for i in range(numCourses):
         credits[i] = self.__courses[i].getCredits()

      totalCredits = sum(credits)
      formattedCredits = [credits for _ in range(numStudents)]

      listMarks = np.array(self.__marks)
      listCredits = np.array(formattedCredits)
      listGPA0 = listMarks*listCredits
      listGPA = [sum(listGPA0[i])/totalCredits for i in range(numStudents)]

      #set the GPAs for students
      for i in range(numStudents):
         self.__students[i].setGPA(listGPA[i])

      #sort the students list by GPAs
      self.__students.sort(reverse = True)

   def printStudents(self):
      numStudents = len(self.__students)
      for i in range(numStudents):
         self.__students[i].print()

   def printMark(self):
      numStudents = len(self.__students)
      numCourses = len(self.__courses)
      for i in range(numStudents):
         for j in range(numCourses):
            print(f"{self.__courses[j].getName()} mark of {self.__students[i].getName()} is {self.__marks[i][j]}")

c = School()
c.input()
c.calGPA()
c.printStudents()