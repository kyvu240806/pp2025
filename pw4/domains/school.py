import math
import numpy as np

from .student import Student
from .course import Course

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