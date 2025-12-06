from .entity import Entity

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